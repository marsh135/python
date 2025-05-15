print("Let's Play Mario Kart!!!")
done = False

def choices(items):
    for i in range(len(items)):
        print(str(items[i]) + " player game")   
    while(True):
        choice = int(input("Choice?: "))
        if(choice>= 0 and choice<=len(items)):
            break
    return choice

        
def choose_kart(kart):
    for item in range(numPlayers):
        playerNumber = 1
        #print(f"Player {numPlayers} ")
        print(karts)
        kartChoice =  input("Player " + str(playerNumber) +": Choose your kart!: ")
        if(kartChoice not in karts):
            print("That character is not available! Choose Again")
        else:
            print("You chose "+ kartChoice +".")
            print(); 
            playerNumber +=1

def choose_character(char):
    playerNumber = 1
    for item in range(numPlayers):
        #print(f"Player {numPlayers} ")
        chosenCharacters = []
        print(characters)
        charChoice =  input("Player " + str(playerNumber) +": Choose your character!: ")
        if(charChoice not in characters):
            print("That character is not available! Choose Again")
        else:
            print("You chose "+ charChoice +". That character is no longer available!")
            characters.remove(charChoice)
            chosenCharacters.append(charChoice)
            print(); 
            playerNumber +=1
            #playerKart = choose_kart(kart)
            
    return chosenCharacters
    

    
            

while(not done):
    players = [1, 2, 3, 4]
    characters = ['Mario',  'Donkey Kong', 'Link', 'Peach', 'Yoshi', 'Bowser']
    karts =  ['Circuit Special', 'Parade', 'Comet', 'Pipe Frame', 'Super Circuit'] 
    motorDisplacement = [50, 100, 150]

    numPlayers =  choices(players)
    print(f"You chose a {numPlayers} player game.")

    playerChoice =  choose_character(characters)
    kartChoice = choose_kart(karts)
    done = True

print("~" * 50)
gL = "Good Luck!!!".center(44, " ")
print(gL); print()
