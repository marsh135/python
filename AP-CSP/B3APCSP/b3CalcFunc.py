def add(a, b):
    return a+b
def sub(a,b):
    return a-b
def mult(a, b):
    return a*b
def div(a,b):
    if b ==0:
        print("INVALID")
    else:
        return a/b
first = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
second = float(input("Enter the second number: "))


if operator == "+":
	result = add(first, second)
elif operator == "-":
	result = sub(first, second)
elif operator == "*":
	result = mult(first, second)
elif operator == "/":
	div(first,second)
else:
	result = "Error: invalid operator"

print(result)
