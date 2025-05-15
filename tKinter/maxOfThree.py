def max_of_two(x,y):
    if x > y:
        return x
    else:
        return y

def max_of_three(x,y,z):
    return max_of_two(x, max_of_two(y,z))

x = int(input("Give me a number: "))
y = int(input("Give me another number: "))
z = int(input("Give me one more number: "))

print(f"The maximum is {max_of_three(x,y,z)}")