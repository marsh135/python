import random

my_list = ["Jarrett A", "Christian K", "Sam D", "Steven E", "Andrew M", "Rielly S", 
           "Kolin H","William S", "Gunnar S", "Patrick", "Cooper", 
           "Joshua", "Cannon", "Link","Ryder", "Xavier", "Sera", "Quinn"]

while my_list:
    selected_items = random.sample(my_list, min(3, len(my_list)))
    for item in selected_items:
        my_list.remove(item)
    print("Selected items:", selected_items)
