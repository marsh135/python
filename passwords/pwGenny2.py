import random
import string
print("Computer Science 2024")
pwLen =  int(input("How many characters for your password?: "))

print('''Choose characters set for the password:
      1. Letters (upper and lower case)
      2. Digits
      3. Punctuation
      4. Exit
      ''')

availableChars = ""


while True:
    choice = int(input("Selection:  "))
    if choice == 1:
        availableChars += string.ascii_letters
        print("You have added letters to your password set")
        print()
    elif choice ==  2:
        availableChars += string.digits
        print("You have added numbers to your password set")
        print()
    elif choice == 3: 
        availableChars += string.punctuation
        print("You have added punctuation to your password set")
        print()
    elif choice == 4: 
        print("Generating password")
        print("-"*20)
        break
    else:
        print("Please pick a valid option")

password = []

for i in range(pwLen):
    randomChar =  random.choice(availableChars)
    password.append(randomChar)

print("The random password is " + "".join(password))

