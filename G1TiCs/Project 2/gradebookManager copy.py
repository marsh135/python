

"""Requirements
1. Create a Gradebook
- Use a dictionary where keys are student names and values are lists of grades.
- Add at least 3 students initially, each with at least 3 grades.
2. User Input
- Allow the user to:
  - Add a new student
  - Add grades for an existing student
  - View the gradebook summary
3. Calculations
- For each student, calculate the average grade.
- Identify and print the student with the highest average.
4. Display
- Print a clear summary of all students, their grades, and their average.
- Example output:
  - Alice: [90, 85, 92] Average: 89.0
  - Bob: [78, 81, 86] Average: 81.7
  - Top Student: Alice
---
5. Additional Features (Required)
- Allow the user to remove a student or a grade.
- Display letter grades (A, B, C, etc.) based on averages.
- Sort students by average grade.
---

Rubric (40 points total)
- 10 pts: Dictionary with students and grades initialized
- 10 pts: User input works to add students and grades
- 10 pts: Correct calculation of averages and top student
- 10 pts: Clear display of gradebook summary

"""
gradebook = {
    "Alice": [90, 85, 92],
    "Bob": [78, 81, 86],
    "Charlie": [88, 90, 84]
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
    sorted_students = sorted(gradebook.items(), key=lambda item: calculate_average(item[1]), reverse=True)
    top_student = None
    highest_average = 0
    for student, grades in sorted_students:
        average = calculate_average(grades)
        letter_grade = get_letter_grade(average)
        print(f"{student}: {grades} Average: {average:.1f} ({letter_grade})")
        if average > highest_average:
            highest_average = average
            top_student = student
    if top_student:
        print(f"Top Student: {top_student} with an average of {highest_average:.1f}")
def add_student():
    name = input("Enter the new student's name: ")
    if name in gradebook:
        print("Student already exists.")
    else:
        gradebook[name] = []
        print(f"Student {name} added.")
def add_grade():
    name = input("Enter the student's name to add a grade: ")
    if name in gradebook:
        try:
            grade = float(input("Enter the grade to add: "))
            if 0 <= grade <= 100:
                gradebook[name].append(grade)
                print(f"Grade {grade} added for {name}.")
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric grade.")
    else:
        print("Student not found.")
def remove_student():
    name = input("Enter the student's name to remove: ")
    if name in gradebook:
        del gradebook[name]
        print(f"Student {name} removed.")
    else:
        print("Student not found.")
def remove_grade():
    name = input("Enter the student's name to remove a grade from: ")
    if name in gradebook:
        try:
            grade = float(input("Enter the grade to remove: "))
            if grade in gradebook[name]:
                gradebook[name].remove(grade)
                print(f"Grade {grade} removed from {name}.")
            else:
                print(f"Grade {grade} not found for {name}.")
        except ValueError:
            print("Invalid input. Please enter a numeric grade.")
    else:
        print("Student not found.")
def main():
    while True:
        print("\nGradebook Manager")
        print("1. View Gradebook Summary")
        print("2. Add New Student")
        print("3. Add Grade for Existing Student")
        print("4. Remove Student")
        print("5. Remove Grade from Student")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")
        if choice == '1':
            display_gradebook()
        elif choice == '2':
            add_student()
        elif choice == '3':
            add_grade()
        elif choice == '4':
            remove_student()
        elif choice == '5':
            remove_grade()
        elif choice == '6':
            print("Exiting Gradebook Manager.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
if __name__ == "__main__":
    main()