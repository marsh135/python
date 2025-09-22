class StudentManager:
    def __init__(self):
        self.students = {}

    def add_student(self, student_id, name):
        if student_id not in self.students:
            self.students[student_id] = {'name': name, 'checked_in': False}
            print(f"Student {name} with ID {student_id} added successfully.")
        else:
            print(f"Student {name} with ID {student_id} already exists.")

    def get_student_name(self, student_id):
        return self.students.get(student_id, {}).get('name', None)

    def get_student_checked_in_status(self, student_id):
        return self.students.get(student_id, {}).get('checked_in', False)


class StudentScanner:
    def __init__(self, student_manager):
        self.student_manager = student_manager

    def check_in(self, student_id):
        if self.student_manager.get_student_checked_in_status(student_id):
            print(f"Student {student_id} is already checked in.")
        else:
            self.student_manager.students[student_id]['checked_in'] = True
            print(f"Student {student_id} checked in successfully.")

    def check_out(self, student_id):
        if self.student_manager.get_student_checked_in_status(student_id):
            self.student_manager.students[student_id]['checked_in'] = False
            print(f"Student {student_id} checked out successfully.")
        else:
            print(f"Student {student_id} is already checked out or not found.")

    def scan_and_confirm(self):
        action = input("Scan 'in' or 'out': ").lower()
        student_id = input("Scan student ID: ")

        if action == 'in':
            self.check_in(student_id)
        elif action == 'out':
            self.check_out(student_id)
        else:
            print("Invalid action. Please enter 'in' or 'out.'")

    def add_student(self):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        self.student_manager.add_student(student_id, name)


if __name__ == "__main__":
    student_manager = StudentManager()
    scanner = StudentScanner(student_manager)

    while True:
        print("\nOptions:")
        print("1. Scan and Confirm")
        print("2. Add Student")
        print("3. Exit")

        choice = input("Select an option (1/2/3): ")

        if choice == '1':
            scanner.scan_and_confirm()
        elif choice == '2':
            scanner.add_student()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
