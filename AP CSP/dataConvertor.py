def d2b(num):
    answer=[]
    num=int(num)
    digit = 0
    if num == 0:
        return 0
    while num > 0 :
        digit =  num %2
        answer.append(str(digit))
        num = num//2
    answer.reverse()
    return "".join(answer)

def d2o(num):
    answer=[]
    digit = 0
    if num == 0:
        return "0"
    while num >0:
        digit =  num %8
        answer.append(str(digit))
        num = num//8
    answer.reverse()
    return "".join(answer)

def d2h(num):
    answer=[]
    digit = 0
    if num == 0:
        return "0"
    while num >0:
        digit =  num %16
        match digit:
            case 10:
                answer.append("A")
            case 11:
                 answer.append("B")
            case 12:
                answer.append("C")
            case 13:
                answer.append("D")
            case 14:
                answer.append("E")
            case 15:
                answer.append("F")
            case _:
                answer.append(str(digit))
        num = num//16
    answer.reverse()
    return "".join(answer)

def decimalTo(num, base):
    digits = "0123456789ABCDEF"
    answer = []

    if num == 0:
        return "0"

    while num > 0:
        remainder = num % base
        answer.append(digits[remainder])
        num //= base

    answer.reverse()
    return "".join(answer)

def b2d(num):
    digits = []
    total = 0
    for i in num:
        digits.insert(0, i)
    for position, digit in enumerate(digits):
        digit = int(digit)
        digit = digit * 2**position
        total += digit
    return total

def o2d(num):
    digits = []
    total = 0
    for i in num:
        digits.insert(0, i)
    for position, digit in enumerate(digits):
        digit = int(digit)
        digit = digit * 8**position
        total += digit
    return total

def h2d(num):
    total =  0
    digits = "0123456789ABCDEF"
    for position, digit in enumerate(num.upper()):
        value = digits.index(digit)
        total += value * 16**(len(num)-position-1)
    return total

def toDecimal(num, base):
    total =  0
    digits = "0123456789ABCDEF"
    for position, digit in enumerate(num.upper()):
        value = digits.index(digit)
        total += value * base**(len(num)-position-1)
    return total

ops = {
    "B": "Decimal to Binary",
    "O": "Decimal to Octal",
    "H": "Decimal to Hexadecimal",
    "b": "Binary to Decimal",
    "o": "Octal to Decimal",
    "h": "Hexadecimal to Decimal"
}
print("DATA CONVERTOR")
print("~"*25)
for op in ops:
    print(op,":", ops[op])
print("Choose a function: ")
oper =  input(">")
while oper not in ops:
    print("Invalid input! Choose a function!  ")
    oper =  input(">")
i = input("Number: ")
#b = int(input("Base: "))
if oper == "B":
    result = d2b(i)
    print(result)
elif oper == "O":
    result = d2o(i)
    print(result)
elif oper == "H":
    result = d2h(i)
    print(result)
elif oper == "b":
    result = b2d(i)
    print(result)
elif oper == "o":
    result = o2d(i)
    print(result)
elif oper == "h":
    result = h2d(i)
    print(result)
