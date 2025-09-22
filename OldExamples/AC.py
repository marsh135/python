import random

def lock_one():
    failed_one = False
    while not failed_one:
        word = random.choice(["whale", "mouse", "horse", "lemur", "bison"])
        letters = list(word)
        correct_letters = []
        print("LOCK ONE:")
        print("   - guess a 5 letter animal: you have 5 incorrect guesses   ")
        print("")
        count = 0
        while len(correct_letters) < 5 and count < 5:
            guessed_letter = input("guess a letter: ")
            if guessed_letter in letters:
                correct_letters.append(guessed_letter)
                print("Correct letters: " + str(", ".join(correct_letters)))
            else:
                count += 1
                print("Try again!")
        if count == 5:
            print("YOU FAILED TO ESCAPE :(")
            failed_one = True
            return False
        else:
            print("Unscramble the letters to find the animal!")
            final_guess = input("Your guess: ")
            while final_guess != word:
                print("Try again!")
                final_guess = input("Your guess: ")
            print("Congratulations! You unlocked LOCK ONE!")
            return True

def lock_two():
    print("LOCK TWO:")
    print("   - solve the riddle in 4 guesses")
    print("")
    print("I have a crown on my head like a king, but I sound a disgrace when I sing. I've fewer eyes on my face than my tail, especially when I'm a male.")
    answer = "peacock"
    count = 0
    while count < 3:
        guess = input("What am I? Your guess: ")
        if guess == answer:
            print("Congratulations! You unlocked LOCK TWO!")
            return True
        else:
            count += 1
            print("Try again!")
    print("YOU FAILED TO ESCAPE :(")
    return False

def lock_three():
    print("LOCK THREE:")
    print("   - solve the math riddle in 4 guesses")
    print("")
    answer = "5"
    count = 0
    while count < 3:
        user_answer = input("A rabbit has 4 legs, and a turtle has 4 legs. If there are 10 animals in the yard, and 5 of them are rabbits, how many are turtles? ")
        if user_answer == answer:
            print("Congratulations! You unlocked LOCK THREE!")
            return True
        else:
            count += 1
            print("Try again!")
    print("YOU FAILED TO ESCAPE :(")
    return False

print("Welcome to SAFARI ESCAPE!")
start = input("Would you like to begin? (select 'yes' or 'no') ")
print("")
if start.lower() == "yes":
    if lock_one():
        print("")
        if lock_two():
            print("")
            lock_three()
else:
    print("Goodbye!")
