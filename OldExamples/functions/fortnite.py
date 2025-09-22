print("Let's Play Fornite!!!")
done = False

def choices(items):
    for i in range(len(items)):
        print(str(items[i]) + " player game")   
    while(True):
        choice = int(input("Choice?: "))
        if(choice>= 0 and choice<=len(items)):
            break
    return choice


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
    return chosenCharacters
    
        
            

while(not done):
    players = [1, 2, 3, 4]
    characters = ['Dark Knight', 'Renegade Raider', 'Recon Expert', 'Peely', 'Bright Bomber', 'Raptor']

    numPlayers =  choices(players)
    print(f"You chose a {numPlayers} player game.")

    playerChoice =  choose_character(characters)
    done = True

print("~" * 50)
gL = "Good Luck!!!".center(44, " ")
print(gL); print()
