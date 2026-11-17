import random
guesses = 10
num =  random.randint(1, 1028)
g = int(input("Guess:" ))

while g !=num:
    if(g>num):
        guesses-=1
        g = int(input("The answer is lower.  Guesses Remaining: "+ str(guesses) +" Guess:" ))
    else:
            guesses-=1
            g = int(input("The answer is higher.  Guesses Remaining: "+ str(guesses) +" Guess:" ))

    if guesses==0:
         print("LOSER)")
print("You got it in", 10-guesses)