import random
import time, sys

start_time = 0
end_time = 0
elapsed = 0

def typewriter(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.05)
    print()

def start(strings):
    global start_time

    letters=[]
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    print("GO")
    print()
    print()
    

    st =  random.choice(strings)

    for l in st:
        letters.append(l)

    print()
    start_time = time.clock_gettime

    print(st)

    return letters

def calcWPM():
    global start_time, end_time, elapsed
    elapsed =  end_time-start_time
    return elapsed

ae = "Two things are infinite: the universe and human stupidity; and I'm not sure about the universe."
sj = "Here's to the crazy ones. The misfits. The rebels. The troublemakers. The round pegs in the square holes. The ones who see things differently. They're not fond of rules. And they have no respect for the status quo. You can quote them, disagree with them, glorify or vilify them. About the only thing you can't do is ignore them. Because they change things. They push the human race forward. And while some may see them as the crazy ones, we see genius. Because the people who are crazy enough to think they can change the world, are the ones who do."
hjb = "Twenty years from now you will be more disappointed by the things that you didn't do than by the ones you did do. So throw off the bowlines. Sail away from the safe harbor. Catch the trade winds in your sails. Explore. Dream. Discover."
strings = [ae, sj, hjb]

ready =  input("Type R to start...").strip().upper()
running = False

while running ==  False:
    if ready == "R":
        cor = start(strings)
        break
    else:
        ready =  input("Type R to start...").strip().upper()

print("Type the string!")
ui = input()
end_time =  time.clock_gettime

uil = []
for l in ui:
    uil.append(l)
points= 0

for i in range(len(uil)):
    if uil[i] == cor[i]:
        points+=1
print(f"Score: {points}")
t = calcWPM
