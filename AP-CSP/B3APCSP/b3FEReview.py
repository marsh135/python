
def analyzeScreenTime(receivedList):
    total = 0
    counter = 0
    for i in receivedList:
        total =  total + i
        counter =  counter +1
    avg =  total/counter
    if avg >=180:
        print("HIGH!")
    elif avg >=90 and avg < 180:
        print("MEDIUM")
    else:
        print("LOW")
sentList = [9,5,12,12,55]
analyzeScreenTime(sentList)
