moods = ["A: Happy", "B: Sad", "C: Calm", "D: Take me away!"]
answers=[]

name= input("What is your name: ")
answers.append(name)
print("How are you feeling today?")
for i in moods:
    print(i)
a1= input("Mood: ")
answers.append(a1)

print(answers)