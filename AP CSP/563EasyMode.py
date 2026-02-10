'''
Title: Trivia Game Helper
Author: Marsh
Description: This is intended to help you get started on 5.6.3
'''
#decalre user score variable and set it to zero
score = 0


#Make a list, called trivia, of AT LEAST 10 dictionaries. Each dictionary should follow the syntax of:
# {"q":"ENTER YOUR QUESTION HERE", "a":"ANSWER"}
#note the "q":"" , "a":"" pairs.  This allows you to CONSISTENTLY access the question using the "q" key and the answer using the 
#"a" key.  Your answers should be either ALL CAPS or all lowers to make validating correct answers later easier

trivia =[
     {"q": "SPORTS: How many players are on the field for each team during a play in football? " , "a":"11"},
     {"q": "SPORTS: How long is a football field in the NFL including endzones?" , "a":"120"},
     {"q": "SPORTS:In basketball, how many points is a free throw worth? " , "a":"1"},
     {"q": "CARS: Which part of the car us used to disconnect the engine from the tranmission in a manual transmission" , "a":"clutch"},
     {"q": "CARS: Which dashboard gauge is used to show how fast the engine in spinning in RPMs" , "a":"tachometer"},
     {"q": "CARS: What is a common component on a gasoline engine that a diesel engine does not use? " , "a":"spark plug"}, 
     {"q": "FOOD:This fruit is the main ingredient in guacamole: " , "a":"avocado"},
     {"q": "FOOD: This italian dish is made from dough, sauce, and cheese: " , "a":"pizza"},
     {"q": "FOOD: What is the byproduct made when fat is extracted from cream to make butter? " , "a":"buttermilk"},     
     {"q": "CS: What data type is the value 23?: " , "a":"int"},
     {"q": "CS: What data type is the value 23.0?" , "a":"double"},
     {"q": "CS: What data type is the value \'23\'? " , "a":"string"}
]
#number of questions - how many items are in the trivia list. This will allow us to do percentages easier
qs = len(trivia)

#main function
def main():
    leaderboard = {}  # create the leaderboard dictionary
    done = False
    while not done: #not False, which is true
        print("==========")  #pretty
        print("S - Start")   # options
        print("D - Display") # option
        print("Q - Quit")  #option
        choice = input("Choice: ").strip().upper()  #get rid of spaces, force their input to be upper case
        if choice == "S":
            print("Starting Game")
            name = input("What's your name? ")
            print("Welcome to the game", name + "!")
            print()

            score = ask(trivia) #call the ask function, written below. Return the score as a value out of the len of trivia
            leaderboard[name] =  score  # add the key value pair to the dictionary. Name is key, score is value

        #quit game case    
        elif choice == "Q":
            print("Exiting Program")
            done = True

        #show the leaderboard
        elif choice == "D":
          for name in leaderboard:
            print(f"Name: {name}   Score:{leaderboard[name]}")


  
def ask(trivia):
  global score
  score = 0
  global qs
  for q in trivia: #each q is a list tiem, in this case, a question dictionary
    print(q["q"]) #print whatever is in that dictionarya t key "q"
    user = input("ANSWER:  ").strip().lower() #all input will be forced to lower case, which matches out "a":"answer" above
    if user == q["a"]:  #check to see if the user input matches the contents of the dictionary at key "a"
      print("Correct!")
      print() #pretty
      score+=1
    else:
      print("Incorrect. The answer was:" , q["a"] +".")  #this does NOT account for spelling mistakes, plurals, etc. If it doesn't match EXACTLY, it is wrong
      print() #pretty
  print(f"Score: {score}   Percentage:{score/qs*100:.2f}%") #show the score. Using an f string for simplicity
  return score #score comes back as an integer value, which we use above
            
main()  # invokes the main method, or function.  VERY common in python and other programming languages
# if fact, Java programs CANNOT execute without the main method. 
#public static void main(String[] args){}
