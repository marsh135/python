def assignment1():
    print("Assignment 1 completed!")
    print()

def assignment2():
    return "Assignment 2 Completed!" 

def execute_assignment(assignment_number):
    #while(assignment_number != "quit"):
    if(assignment_number == "1"):
        assignment1()
    elif(assignment_number == "2"):
        print(assignment2())
    #elif(assignment_number ==  'quit'):
        #return
    assignment_number =  input("Choose an assignment: ")


        

