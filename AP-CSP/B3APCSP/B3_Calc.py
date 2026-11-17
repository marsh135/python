def add(x, y):
  return x + y 
def sub(x, y):
  return x - y 
def mult(x,y):
  return x * y 
def div(x, y):
  return x / y 
def idiv(x, y):
  return x // y 
def exp(x, y):
  return x**y 

while True:
  a = int(input("First number: "))
  op = input("Please choose an operation:  +  -  *  /  //  **  ").strip()
  b = int(input("Second number: "))

  
  if( op == "+"):
    res = add(a, b)
  elif( op == "-"):
    res =  sub(a,b)
  elif(op == "*"):
    res = mult(a, b)
  elif(op == "/"):
    res = div(a,b)
  elif(op == "//"):
    res = idiv(a, b)
  elif(op == "**"):
    res = exp(a, b)
  else:
    print("INVALID!")
  
  print()
  print(a,op,b,"=",res)
  print("-_"*10)
  print()

  
