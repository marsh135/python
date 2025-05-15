import random

while input != "quit" :
    num = int(input("How many sides to your dice? Type 0 to quit: "))
    for i in range(num):
        random_int = random.randint(1, num)

    print("You rolled a " + str(random_int) + " on a d" + str(num)+ ".")
print("Thanks for playing!")