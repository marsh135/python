# Global variable
x = 10

def modify_variable():
    global x  # Access the global variable
    x += 5
    print("Inside function, global x:", x)

def use_local_variable():
    y = 20  # Local variable
    print("Inside function, local y:", y)

# Main program
print("Before function call, global x:", x)
modify_variable()
print("After function call, global x:", x)
use_local_variable()