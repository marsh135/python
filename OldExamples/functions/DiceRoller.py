import random

DICE_ART = {
    1: (
        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",
    ),
    2: (
        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",
    ),
    3: (
        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",
    ),
    4: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    5: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",
    ),
    6: (
        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",
    )
}
DIE_HEIGHT =  len(DICE_ART[1])
DIE_WIDTH =  len(DICE_ART[1][0])
DIE_FACE_SEPARATOR = ""

def parseInput(input_string):
    options = ['1', '2', '3', '4', '5', '6']
    while True:
        if input_string.strip() in options:
            return int(input_string)
            break
        
        else:
            print("Please enter a number form 1 to 6.")
            raise SystemExit(1)

def roll_dice(numDice):
    roll_results = []
    for i in range(numDice):
        roll  = random.randint(1,6)  
        roll_results.append(roll)
    return roll_results          

def generateDieFaces(dice_values):
    dice_faces = []
    for value in dice_values:
        dice_faces.append(DICE_ART[value])
    
    dice_faces_rows = []
    
    for row_idx in range(DIE_HEIGHT):
        row_components = []
        for die in dice_faces:
            row_components.append(die[row_idx])
        row_string =  DIE_FACE_SEPARATOR.join(row_components)
        dice_faces_rows.append(row_string)
    
    width =  len(dice_faces_rows[0])
    diagram_header =  " RESULTS ".center(width, "~")

    dice_faces_diagram = "\n".join([diagram_header] + dice_faces_rows)
    return dice_faces_diagram

numDiceInput = input("How many dice would you like to roll [1-6]? : ")
numDice =  parseInput(numDiceInput)

roll_results = roll_dice(numDice)

dice_face_diagram =  generateDieFaces(roll_results)

print(f"\n{dice_face_diagram}")



