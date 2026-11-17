#this app needs to collect two numbers
#from the user
#It will then compare the two numbers and output which one is greater
#if they are equal, return equal


while True:

    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    dynamite = num1 + num2

    if num1 > num2:
        print(str(num1) + " is greater than " + str(num2) + ".")
    elif num2 > num1:
        print(str(num2) + " is greater than " + str(num1) + ".")
    else:
        print("Those numbers are equal!")