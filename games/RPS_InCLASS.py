import random

p1s = 0
p2s = 0

players = int(input("How many players? 1 or 2: "))

if players == 1:

  while p1s !=5 and p2s !=5:
    p1 =  int(input("Choose Rock(1), Paper(2), or Scissors(3)"))
    p2 =  random.randint(1,3)
    if p1 == p2:
      print("TIE")
    elif p1 == 1 and p2 == 3  or p1 == 2 and p2 == 1 or p1 == 3 and p2 == 2:
      print("winner!")
      p1s+=1
    else:
      print("You lose!")
      p2s+=1
  else:
    if p1s ==5:
      print("player one wins the game")
    else:
      print("Player 2 won this round!")

elif players == 2:

  while p1s !=5 and p2s !=5:
    p1 =  int(input("Player 1: Choose Rock(1), Paper(2), or Scissors(3)"))
    p2 =  int(input("Player 2: Choose Rock(1), Paper(2), or Scissors(3)"))
    if p1 == p2:
      print("TIE")
    elif p1 == 1 and p2 == 3  or p1 == 2 and p2 == 1 or p1 == 3 and p2 == 2:
      p1s+=1
      print(f"Player 1 Wins!  {p1s} - {p2s}")
      
    else:
       p2s+=1
       print(f"Player 2 Wins!   {p1s} - {p2s}")
     
  else:
    if p1s ==5:
      print(f"player one wins the game -  {p1s} - {p2s}")
    else:
      print(f"Player 2 won this round!  - {p1s} - {p2s}")
