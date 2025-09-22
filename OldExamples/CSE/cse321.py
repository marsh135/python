'''

string_list = ["W", "or", "l", "d!"]
int_list = [5, 15, -67, 191, 88, -23]
float_list = [2.2, -101.9, 60.0]
boolean_list = [False, False, True, False, True]
mixed_list = ["Hello", 2, "the", string_list]
empty = []

print(string_list)


'''


# a list of menu items
food = ["Burger", "Shake", "Fries", "Sundae", "last item"]
item = 0

'''
for i in range(0, len(food)):
    menu_item = food[item]
    print(menu_item, "is located at index " + str(item) +".")
    item+=1
print(food[-1] + " is located at index -1.")


if ("Sundae" in food):
  print("One sundae, coming up!")
else:
  print("Sorry, we don't carry sundaes")'''

'''

if ("Pizza" in food):
  print("One pizza, coming up!")
else:
  print("Sorry, we don't carry pizza")

print(food[-1])'''


customer_order = ["Fries", "Shake"] 
item = input("What else would you like to order? ") 
customer_order.append(item) 

print("You ordered", customer_order) 
answer = input("Is your order correct? ") 
if (answer == "yes"): 
  print("Great! Your order is coming right up!") 
else: 
  print("Okay, I will remove", item, "from your order.") 
  customer_order.remove(item) 

print("Your new order is", customer_order)