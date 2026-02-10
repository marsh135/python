'''
Title: Trivia Game Helper
Author: Marsh
Description: This is intended to help you get started on 5.6.3
'''

score = 0
qs = 0
trivia ={
"sports":
    [
     {"q": "How many players are on the field for each team during a play in football? " , "a":"11"},
     {"q": "How long is a football field in the NFL including endzones?" , "a":"120"},
     {"q": "In basketball, how many points is a free throw worth? " , "a":"1"}
    ],
  "cars":[
      {"q": "Which part of the car us used to disconnect the engine from the tranmission in a manual transmission" , "a":"clutch"},
      {"q": "Which dashboard gauge is used to show how fast the engine in spinning in RPMs" , "a":"tachometer"},
      {"q": "What is a common component ona  gasoline engine that a diesel engine does not use? " , "a":"spark plugs"}  
    ],
  "food":[
     {"q": "This fruit is the main ingredient in guacamole: " , "a":"avocado"},
     {"q": "This italian dish is made from dough, sauce, and cheese: " , "a":"pizza"},
     {"q": "What is the byproduct made when fat is extracted from cream to make butter? " , "a":"buttermilk"}     
    ],
  "cs":[
     {"q": "What data type is the value 23?: " , "a":"int"},
     {"q": "What data type is the value 23.0?" , "a":"double"},
     {"q": "What data type is the value \'23\'? " , "a":"string"}     
    ]
}

def main():
    leaderboard = {}
    done = False
    while not done:
        print("==========")
        print("S - Start")
        print("D - Display")
        print("Q - Quit")
        choice = input("Choice: ")
        if choice == "S":
            print("Starting Game")
            name = input("What's your name? ")
            print("Welcome to the game", name + "!")
            print()
            for cat in trivia:
              print(cat)
            catChoice = input("Which category would you like?").strip().lower()
            score = ask(trivia, catChoice)
            leaderboard[name] =  score
        elif choice == "Q":
            print("Exiting Program")
            done = True
        elif choice == "D":
          for name in leaderboard:
            print(name, leaderboard[name])


  
def ask(trivia, cat):
  score = 0
  qs = 0
  for q in trivia[cat]:
    qs+=1
    print(q["q"])
    user = input("ANSWER:  ").strip().lower()
    if user == q["a"]:
      print("Correct!")
      print()
      score+=1
    else:
      print("Incorrect. The answer was:" , q["a"] +".")
      print()
  print(f"Score: {score}   Percentage:{score/qs*100:.2f}%")
  return score
            
main()
