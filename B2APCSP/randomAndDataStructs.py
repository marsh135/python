import random

#my_list = [1,2,3,4,5,6]
print(random.randint(1,6))


caps ={
    "IN":"Indianapolis",
    "OH":"Columbus",
    "KY":"Frankfort",
    "IL":"Springfield",
    "WI":"Madison",
    "MI":"Lansing"
}
for key in caps:
    print(key)

choice = input("Enter a state abbreviation: ")
if(choice == "IN"):
    print(caps["IN"])
elif(choice == "OH"):
    print(caps["OH"])
elif(choice == "KY"):
    print(caps["KY"])