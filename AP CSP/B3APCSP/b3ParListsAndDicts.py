print("Welcome to the B3 Diner!!")
menu={
    "Pancakes": 1.25,
    "Steak": 8.00,
    "Bacon": 2.25,
    "Eggs": 1.25,
    "Waffles": 6.00,
    "Hamburger": 5.96
}
running = True
while running:
    for i in menu:
        print(i)
    choice= input("What would you like:  ").strip().capitalize()
    if choice in menu:
        print("Our", choice, "costs $" + str(menu[choice])+".")

    else:
        print("We do not have that!")
    more =  input("Does that complete your order? Y/N  ").strip().upper()
    if more == "Y":
        running= False
print("--"*10)
print("We will have that out to you shortly")




'''print("Welcome to the B3 Diner!!")
menu = ["", "Pancakes", "Steak", "Bacon", "Eggs", "Waffles", "Hamburger"]
prices=[0, 1.25, 8.95, 2.00, 1.25, 4.15, 5.96]
for i in range(1,len(menu)):
    print(i, "Item:", menu[i],"    Price: $"+ str(prices[i]))
'''

