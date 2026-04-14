import hashlib
import json
import os

PASSWORDS_FILE = "passwords.json"
passwords = {}

def save_passwords():
    with open(PASSWORDS_FILE, 'w') as f:
        json.dump(passwords, f)

def load_passwords():
    global passwords
    if os.path.exists(PASSWORDS_FILE):
        with open(PASSWORDS_FILE, 'r') as f:
            passwords = json.load(f)

def store_password(username, password):
    passwords[username] = hashlib.sha256(password.encode()).hexdigest()
    save_passwords()
    
def get_password(username):
    return passwords.get(username, None)    

def create_user():
    username = input("Enter a username: ")

    if username in passwords:
        print("Username already exists. Please choose a different username.")
    else:
        password = input("Enter a password: ")
        store_password(username, password)
        print("User created successfully.")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    stored_password = get_password(username)

    if stored_password is None:
        print("Username not found.")
    elif stored_password == password:
        print("Login successful!")
    else:
        print("Incorrect password.")

def login_hashed():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    stored_password = get_password(username)

    if stored_password is None:
        print("Username not found.")
    else:
        hashed_input = hashlib.sha256(password.encode()).hexdigest()

        if stored_password == hashed_input:
            print("Login successful!")
        else:
            print("Incorrect password.")

def print_passwords():
    print("Stored passwords:")
    for username, password in passwords.items():
        print(f"{username}: {password}")

def main():
    load_passwords()
    
    while True:
        print("\n1. Create User")
        print("2. Login")
        print("3. Print Passwords")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            create_user()
        elif choice == '2':
            login_hashed()
        elif choice == '3':
            print_passwords()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()