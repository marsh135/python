import random, time
def typewriter(answer):
    for i in range(3):
        print("thinking...")
        time.sleep(random.randint(2,8)/10)
    print("-"*25)
    for l in answer:
        print(l, end="", flush=True)
        time.sleep(.1)
    print()
eB={
    1:"Ask again later",
    2:"Fo Sho",
    3:"Prolly not...",
    4:"Possibly, but I wouldn\'t bet on it",
    5:"DEF",
    6:"Yes",
    7:"Nah, twin...",
    8:"Bruh...."
}
shaking = True
while shaking:
    ui = input("What would you like to know?:  \n")
    answer = (eB[random.randint(1,8)])
    if(answer == "Bruh...."):
        typewriter("I am so done with this crap...")
        shaking =  False
        break
    typewriter(answer)
    again = input("Would you like to ask another question?  (Y/N)").strip().upper()
    match again:
        case "Y":
            shaking = True
        case "N":
            shaking = False
            print("DESTINY AWAITS")
        case _:
            print("INVALID")