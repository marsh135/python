import pandas as pd
import random

# Sample data
first_names = ["John", "Jane", "Alex", "Emily", "Chris", "Katie", "Michael", "Sarah", "David", "Laura", "Daniel", "Emma", "James", "Olivia", "Ethan", "Sophia", "Matthew", "Isabella", "Andrew", "Mia","Joseph", "Charlotte", "Samuel", "Amelia", "Benjamin", "Harper", "Elijah", "Evelyn", "Lucas", "Abigail"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin","Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson"]
majors = ["Mathematics", "Science", "Business", "Art", "Engineering", "History", "Literature", "Computer Science", "Biology", "Chemistry", "Physics", "Economics", "Psychology", "Sociology", "Philosophy"]
years = ["Freshman", "Sophomore", "Junior", "Senior", "Graduate"]
names = []
for i in range(1000000):
    names.append(f"{random.choice(first_names)} {random.choice(last_names)}")

# Generate random student data
data = {
    "Name": names,
    "Age": [random.randint(18, 25) for _ in names],
    "GPA": [round(random.uniform(2.0, 4.0), 2) for _ in names],
    "Sports_Played": [random.randint(0, 3) for _ in names],
    "Credits_Completed": [random.randint(0, 120) for _ in names], 
    "Major":[random.choice(majors) for _ in names],
    "Year":[random.choice(years) for _ in names]
}

students_df = pd.DataFrame(data)

#print(round(students_df.describe()))

students_df.to_csv('students_data1000000.csv', index=False) # Save to CSV file
#print("DataFrame saved to 'students_data.csv'")