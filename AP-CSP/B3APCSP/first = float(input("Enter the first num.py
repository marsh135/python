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
	if second == 0:
		result = "Error: cannot divide by zero"
	else:
		result = first / second
else:
	result = "Error: invalid operator"

print(result)
