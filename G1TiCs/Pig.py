import random
turn = "Player1"
p1 = 0
p2 = 0 
total = 0

def roll():
    global total
    roll = random.randint(1,6)
    print(roll)
    if(roll == 1): 
        total = 0
        print(total)
    else: 
        total+=roll
        print(total)

def reset():
    global total
    total=0
def hold():
    global total, p1, p2, turn
    if(turn == "Player1"):
        p1+=total
        print("Player 1 holds. SCORE: ", p1)
        print("It's your turn, P2!)")
        turn= "Player2"
    else:
        p2+=total
        print("Player 2 holds. SCORE: ", p2)
        print("It's your turn, P1!")
        turn= "Player1"
    reset()

def play():
    print("\nPlayer 1 score:", p1, "Player 2 score:", p2, "Turn total:", total)
    choice = input(f"{turn}, would you like to (r)oll or (h)old? ").lower().strip()

    if choice == "r":
        roll()
    elif choice == "h":
        hold()
    else:
        print("INVALID choice.")

def end():
    if p1 >=100:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")


print("Welcome to the Game of Pig!")
while p1 <100 and p2<100:
    play()
end()
    
