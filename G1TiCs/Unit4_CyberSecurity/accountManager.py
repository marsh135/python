import json
import os
from getpass import getpass
from hashlib import sha256
from pathlib import Path


DATA_FILE = Path(
    os.environ.get(
        "ACCOUNT_MANAGER_DATA_FILE",
        Path(__file__).with_name("account_manager_data.json"),
    )
)


def hash_text(text):
    return sha256(text.encode("utf-8")).hexdigest()


class Account:
    def __init__(self, site, username, password):
        self.site = site
        self.username = username
        self.password = password

    def display(self):
        return f"Site: {self.site}, Username: {self.username}"

    def to_dict(self):
        return {
            "site": self.site,
            "username": self.username,
            "password": self.password,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["site"], data["username"], data["password"])


class PasswordManager:
    def __init__(self, master_password, accounts=None, data_file=DATA_FILE, is_hashed=False):
        self.master_password_hash = master_password if is_hashed else hash_text(master_password)
        self.accounts = accounts or []
        self.data_file = Path(data_file)

    def login(self, entered_password):
        return hash_text(entered_password) == self.master_password_hash

    def find_account(self, site):
        for account in self.accounts:
            if account.site.lower() == site.lower():
                return account
        return None

    def add_account(self, site, username, password):
        if self.find_account(site):
            print(f"An account for {site} already exists.")
            return False

        self.accounts.append(Account(site, username, password))
        self.save()
        print(f"Account for {site} added.")
        return True

    def view_accounts(self):
        if len(self.accounts) == 0:
            print("No accounts stored.")
            return

        for index, account in enumerate(self.accounts, start=1):
            print(f"{index}. {account.display()}")

    def get_password(self, site):
        account = self.find_account(site)
        if account:
            print(f"Password for {account.site}: {account.password}")
            return account.password

        print("Account not found.")
        return None

    def update_account(self, site, username=None, password=None):
        account = self.find_account(site)
        if not account:
            print("Account not found.")
            return False

        if username:
            account.username = username
        if password:
            account.password = password

        self.save()
        print(f"Account for {account.site} updated.")
        return True

    def delete_account(self, site):
        account = self.find_account(site)
        if not account:
            print("Account not found.")
            return False

        self.accounts.remove(account)
        self.save()
        print(f"Account for {account.site} deleted.")
        return True

    def save(self):
        data = {
            "master_password_hash": self.master_password_hash,
            "accounts": [account.to_dict() for account in self.accounts],
        }
        self.data_file.write_text(json.dumps(data, indent=4), encoding="utf-8")

    @classmethod
    def load(cls, data_file=DATA_FILE):
        path = Path(data_file)
        if not path.exists():
            return None

        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            print("Saved data could not be loaded. Starting a new vault.")
            return None

        accounts = []
        for item in data.get("accounts", []):
            if isinstance(item, dict):
                try:
                    accounts.append(Account.from_dict(item))
                except KeyError:
                    continue

        master_password_hash = data.get("master_password_hash", "")
        if not master_password_hash:
            return None

        return cls(
            master_password_hash,
            accounts=accounts,
            data_file=path,
            is_hashed=True,
        )


def prompt_non_empty(prompt_text):
    while True:
        value = input(prompt_text).strip()
        if value:
            return value
        print("This field cannot be empty.")


def prompt_new_password():
    while True:
        password = getpass("Create a master password: ")
        confirm_password = getpass("Confirm master password: ")

        if not password:
            print("Password cannot be empty.")
        elif password != confirm_password:
            print("Passwords did not match. Try again.")
        else:
            return password


def load_or_create_manager():
    manager = PasswordManager.load()
    if manager is not None:
        return manager

    print("No saved vault found. Create a master password to get started.")
    master_password = prompt_new_password()
    manager = PasswordManager(master_password)
    manager.save()
    print("Vault created.")
    return manager


def show_menu():
    print("\nPassword Manager")
    print("1. Add account")
    print("2. View accounts")
    print("3. Show password")
    print("4. Update account")
    print("5. Delete account")
    print("6. Exit")


def run_password_manager():
    manager = load_or_create_manager()

    for attempt in range(3):
        entered_password = getpass("Enter master password: ")
        if manager.login(entered_password):
            print("Access granted.")
            break
        print("Access denied.")
    else:
        print("Too many failed attempts.")
        return

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            site = prompt_non_empty("Site: ")
            if manager.find_account(site):
                print("That site is already stored. Use update instead.")
                continue

            username = prompt_non_empty("Username: ")
            password = getpass("Password: ")
            if not password:
                print("Password cannot be empty.")
                continue

            manager.add_account(site, username, password)
        elif choice == "2":
            manager.view_accounts()
        elif choice == "3":
            site = prompt_non_empty("Site to look up: ")
            manager.get_password(site)
        elif choice == "4":
            site = prompt_non_empty("Site to update: ")
            account = manager.find_account(site)
            if not account:
                print("Account not found.")
                continue

            new_username = input(f"New username [{account.username}]: ").strip()
            new_password = getpass("New password (leave blank to keep current): ")
            manager.update_account(
                site,
                username=new_username or account.username,
                password=new_password or account.password,
            )
        elif choice == "5":
            site = prompt_non_empty("Site to delete: ")
            confirm = input(f"Delete account for {site}? (y/n): ").strip().lower()
            if confirm == "y":
                manager.delete_account(site)
            else:
                print("Delete cancelled.")
        elif choice == "6":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Enter 1-6.")


if __name__ == "__main__":
    run_password_manager()
