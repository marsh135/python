import random

choices = ['rock', 'paper', 'scissors']


def get_user_choice():
    while True:
     user_choice = input("Choose rock, paper, or scissors: ").lower().strip()
     if user_choice in choices:
        return user_choice 
     else:
        print("Invalid choice. Pleae choose rock, paper, or scissors!")

def get_computer_choice():
    return random.choice(choices)


def logic(user_choice, computer_choice):
   if user_choice == computer_choice:
        return "It's a tie!"
   elif user_choice == "rock" and computer_choice == "scissors" or user_choice == "paper" and computer_choice == "rock" or user_choice == "scissors" and computer_choice == "paper":
        return "You win!"
   else:
      return "Computer wins!"



def play():
     user_choice =  get_user_choice()
     computer_choice =  get_computer_choice()
     print("You chose " + user_choice + " and the computer chose " + computer_choice +".")
     result = logic(user_choice, computer_choice)
     print(result)

while True:
    play()
    #play_again = input("Play again? Yes or no: ").strip().lower()
    #if play_again == 'no':
       #break
