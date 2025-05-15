x = int(input("Give me a number: "))
y = int(input("Give me another number: "))
z = int(input("Give me one more number: "))

greatest_num =  0

if x > y and x > z:
    greatest_num= x
    print("x is biggest" + str(x))
elif y>z and y> x:
    greatest_num = y
    print("y is biggest" + str(y))
else:
    greatest_num =z
    print("z is biggest" + str(z))


