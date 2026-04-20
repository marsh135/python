

#Create a Python program to manage student grades using lists, tuples, and dictionaries. 
#This project will give you practice with:
##- Variables and data types
#- Lists and dictionaries
#- Loops and conditionals
#- User input
#- Calculating averages and summaries

#---

#Requirements
#1. Create a Gradebook
#- Use a dictionary where keys are student names and values are lists of grades.
#- Add at least 3 students initially, each with at least 3 grades.
#2. User Input
#- Allow the user to:
#  - Add a new student
#  - Add grades for an existing student
#  - View the gradebook summary
#3. Calculations
#- For each student, calculate the average grade.
#- Identify and print the student with the highest average.
#4. Display
#- Print a clear summary of all students, their grades, and their average.
#- Example output:
#  - Alice: [90, 85, 92] Average: 89.0
#  - Bob: [78, 81, 86] Average: 81.7
#  - Top Student: Alice
#---
#5. Additional Features (Required)
#- Allow the user to remove a student or a grade.
#- Display letter grades (A, B, C, etc.) based on averages.
# Sort students by average grade.
#---

#Rubric (40 points total)
#- 10 pts: Dictionary with students and grades initialized
#- 10 pts: User input works to add students and grades
#- 10 pts: Correct calculation of averages and top student
#- 10 pts: Clear display of gradebook summary

# Initialize the gradebook with some students and their grades
gradebook = {
    "Alice": [90, 85, 92],
    "Bob": [78, 81, 86],
    "Charlie": [88, 90, 91]
}
def calculate_average(grades):
    return sum(grades) / len(grades) if grades else 0
def get_letter_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'
def display_gradebook():
    print("\nGradebook Summary:")
    top_student = None
    highest_average = 0
    for student, grades in gradebook.items():
        average = calculate_average(grades)
        letter_grade = get_letter_grade(average)
        print(f"{student}: {grades} Average: {average:.2f} ({letter_grade})")
        if average > highest_average:
            highest_average = average
            top_student = student
    if top_student:
        print(f"Top Student: {top_student} with an average of {highest_average:.2f}")
def add_student():
    name = input("Enter the new student's name: ")
    if name in gradebook:
        print(f"Student {name} already exists.")
    else:
        gradebook[name] = []
        print(f"Student {name} added.")
def add_grade():
    name = input("Enter the student's name to add a grade: ")
    if name in gradebook:
        try:
            grade = float(input(f"Enter the grade to add for {name}: "))
            if 0 <= grade <= 100:
                gradebook[name].append(grade)
                print(f"Grade {grade} added for {name}.")
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric grade.")
    else:
        print(f"Student {name} not found.")
        
