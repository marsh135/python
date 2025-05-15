import random

#define function/subroutine

def dice_roller(numSides):
    result = random.randint(1, numSides)
    return result
    #print(f"You rolled a {result}.")

numSides =  int(input("How many sides? :  "))

output = dice_roller(numSides)

#print("You rolled a " + str(output))
print(f"You rolled a {output}.")