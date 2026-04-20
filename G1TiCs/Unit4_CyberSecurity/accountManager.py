class Account:
    def __init__(self, site, username, password):
        self.site = site
        self.username = username
        self.password = password

    def display(self):
        return f"Site: {self.site}, Username: {self.username}"


class PasswordManager:
    def __init__(self, master_password):
        self.master_password = master_password
        self.accounts = []   # list of Account objects

    def login(self, entered_password):
        return entered_password == self.master_password

    def add_account(self, site, username, password):
        new_account = Account(site, username, password)
        self.accounts.append(new_account)
        print(f"Account for {site} added.")

    def view_accounts(self):
        if len(self.accounts) == 0:
            print("No accounts stored.")
        else:
            for account in self.accounts:
                print(account.display())

    def get_password(self, site):
        for account in self.accounts:
            if account.site.lower() == site.lower():
                print(f"Password for {site}: {account.password}")
                return
        print("Account not found.")