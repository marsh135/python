print("Welcome to our Diner!")
print("~"*30)

diner ={
    "A: pancakes": 4.99,
    "B: eggs": 2.00,
    "C: waffles": 4.99,
    "CB w/ f": 10.00,
    "Surf and Turrrf": 2.99
}
print(diner)
uc =  input("Choose: " )

print(diner[uc])
'''
menu = ["Pancakes", "Eggs", "Waffles", "Cheeseburger w/ fries"]
prices = [4.99,2.00,4.99, 10.00]

for i in range(len(menu)):
    print("Item: ", menu[i], "   Price: $"+ str(prices[i]))
'''