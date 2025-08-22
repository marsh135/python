# Daily Mood Tracker

# <List code segment-1>
# Initializes a list to store user moods for each day of the week
mood_list = []

# <Procedure code segment-1>
def record_mood(day, mood):  
    #Records the user's mood for a given day and stores it in the list.
    
    entry = f"{day}: {mood}"  
    if mood.lower() not in ['happy', 'sad', 'neutral', 'angry']:  # selection
        print("Invalid mood. Please use: happy, sad, neutral, angry.")
        return
    mood_list.append(entry)  
    print(f"Recorded: {entry}")

# <Procedure code segment-2>
# Calling the procedure with input
for i in range(7):  
    day = input("Enter day: ")
    mood = input("Enter your mood (happy/sad/neutral/angry): ")
    record_mood(day, mood)

# <List code segment-2>
# Process mood list to find the most common mood
def analyze_moods():
    mood_count = {"happy": 0, "sad": 0, "neutral": 0, "angry": 0}
    for entry in mood_list: 
        mood = entry.split(": ")[1]
        if mood in mood_count:  
            mood_count[mood] += 1

    most_common = max(mood_count, key=mood_count.get)
    print(f"The most common mood this week was: {most_common}")

# Final Output
analyze_moods()

# THIS CODE WAS PRODUCED ENTIRELY BY Chat.gpt 