#create a list

def calcAvg(mml):
    total = 0
    counter = 0
    for i in mml:
        total=total+i
        counter=  counter + 1
        #counter+=1
    avg =  total/counter
    if avg >= 180:
        print("HIGH")
    elif avg >=90 and avg <180:
        print("MID")
    else:
        print("LOW")


minutesListened = [45,56,87,95,28]
calcAvg(minutesListened)