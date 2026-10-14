first = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
second = float(input("Enter the second number: "))

if operator == "+":
	result = first + second
elif operator == "-":
	result = first - second
elif operator == "*":
	result = first * second
elif operator == "/":
	result = "Cannot divide by zero" if second == 0 else first / second
else:
	result = "Invalid operator"

print(result)
