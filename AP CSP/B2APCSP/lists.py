mylist = ["apples", "bananas", "cherries", "dragonfruit", "elderberry", "fig"]

print("Hello, welcome to our store!\nWhat are you looking for?")
item = int(input().strip().lower())

if item in mylist:
    print("We have", item)
else:
    print("Sorry, we are out of", item)














'''

mylist.remove("apples") #remove
print("REMOVE - "*5)
for i in mylist:
    print(i)

mylist.append("apples")#append
print("APPEND ~"*5)
for i in mylist:
    print(i)

mylist.insert(2,"apples")#append
print("INSERT - "*5)
for i in mylist:
    print(i)


mylist.pop(1)
print("POP ~"*5)
for i in mylist:
    print(i)

'''