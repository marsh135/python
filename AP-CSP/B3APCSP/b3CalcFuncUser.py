"""Simple four-operation calculator without using def statements."""

add = lambda a, b: a + b
subtract = lambda a, b: a - b
multiply = lambda a, b: a * b
divide = lambda a, b: a / b

print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
choice = input("Choose an operation: ")
first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))

operations = {
	"1": add,
	"2": subtract,
	"3": multiply,
	"4": divide,
}

if choice not in operations:
	print("Invalid operation")
elif choice == "4" and second == 0:
	print("Cannot divide by zero")
else:
	print("Result:", operations[choice](first, second))
