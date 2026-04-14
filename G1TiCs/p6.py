import hashlib
import json
import os

DATA_FILE = "password_manager.json"
data = {"users": {}}


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def load_data():
    global data
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)


def create_user():
    username = input("Enter a username: ")

    if username in data["users"]:
        print("That username already exists.")
        return

    password = input("Enter a master password: ")
    hashed_password = hash_password(password)

    data["users"][username] = {
        "master_password": hashed_password,
        "vault": {}
    }

    save_data()
    print("User created successfully.")


def login():
    username = input("Enter your username: ")
    password = input("Enter your master password: ")

    if username not in data["users"]:
        print("Username not found.")
        return None

    hashed_input = hash_password(password)
    stored_hash = data["users"][username]["master_password"]

    if hashed_input == stored_hash:
        print("Login successful!")
        return username
    else:
        print("Incorrect password.")
        return None


def add_entry(current_user):
    account_name = input("Enter the account name (example: gmail): ")
    account_password = input("Enter the password for that account: ")

    data["users"][current_user]["vault"][account_name] = account_password
    save_data()
    print(f"Password for '{account_name}' saved.")


def retrieve_entry(current_user):
    account_name = input("Enter the account name to retrieve: ")

    vault = data["users"][current_user]["vault"]

    if account_name in vault:
        print(f"Password for '{account_name}': {vault[account_name]}")
    else:
        print("No password stored for that account.")


def view_account_names(current_user):
    vault = data["users"][current_user]["vault"]

    if not vault:
        print("No stored accounts yet.")
        return

    print("Stored account names:")
    for account_name in vault:
        print(f"- {account_name}")


def user_menu(current_user):
    while True:
        print(f"\n--- Password Vault for {current_user} ---")
        print("1. Add a password")
        print("2. Retrieve a password")
        print("3. View stored account names")
        print("4. Log out")

        choice = input("Select an option: ")

        if choice == "1":
            add_entry(current_user)
        elif choice == "2":
            retrieve_entry(current_user)
        elif choice == "3":
            view_account_names(current_user)
        elif choice == "4":
            print("Logging out.")
            break
        else:
            print("Invalid choice. Try again.")


def main():
    load_data()

    while True:
        print("\n--- Password Manager ---")
        print("1. Create User")
        print("2. Login")
        print("3. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            create_user()
        elif choice == "2":
            current_user = login()
            if current_user is not None:
                user_menu(current_user)
        elif choice == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()