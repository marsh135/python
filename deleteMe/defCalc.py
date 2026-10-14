def add(a, b):
    return a+b
def sub(a,b):
    return a-b
def mult(a,b):
    return a*b
def div(a,b):
    if b==0:
        return("Cannot divide by 0")
    else:
        return a/b

f = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
s = float(input("Enter the second number: "))

if operator == "+":
	result = add(f,s)
elif operator == "-":
	result = sub(f,s)
elif operator == "*":
	result = mult(f,s)
elif operator == "/":
	result = div(f,s)
print(result)