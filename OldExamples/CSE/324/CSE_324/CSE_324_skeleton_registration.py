from CSE_324_course import Course
from CSE_324_skeleton_student import Student
from CSE_324_assignments import *

studentList = []

math = Course("Algebra I")
language = Course("Spanish I")
science = Course("Earth Science")
history = Course("U.S. History I")
phys_ed = Course("Physical Education I")
comp_sci = Course("Computer Science")
robs =  Course("Robotics")


test_student = Student("Jessica", "Rose")

test_student.add_course(math)
test_student.add_course(language)
test_student.add_course(science)
test_student.add_course(history)

studentList.append(test_student)

test_student2 = Student("Cooper", "Wallace")

test_student2.add_course(math)
test_student2.add_course(phys_ed)
test_student2.add_course(science)
test_student2.add_course(history)

studentList.append(test_student2)


test_student3 = Student("Kyle", "Marsh")

test_student3.add_course(math)
test_student3.add_course(comp_sci)
test_student3.add_course(phys_ed)
test_student3.add_course(robs)

studentList.append(test_student3)


#TODO Add all the test students to a list of your own creation


#TODO print student_list
for i in studentList:
    print(i)
    
#TODO iterate over each of the students in the list and print their names and course schedules.
    #Each iteration should:
        #print the student
#assignment1()
#assignment2_result = assignment2()
#print(assignment2_result)

#assignment_number =  input("Choose an assignment: ")

#execute_assignment(assignment_number)

print("Student List")
print("~"*50)
for s in studentList:
    s.print_student_no_courses()