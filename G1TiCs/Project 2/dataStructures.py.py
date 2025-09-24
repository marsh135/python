

#Part 1: Lists
#1. Create a list of 10 numbers.
#2. Print the first, last, and middle number.
#3. Add a new number to the end of the list.
#4. Replace the third number with 99.
#5. Loop through the list and print only the even numbers.

my_list =  [2, 8,13, 8, 1, 9, 4, 6, 7, 10]
print(my_list[0])
print(my_list[-1])
print(my_list[len(my_list)//2])
my_list.append(11)
my_list[2] = 99
for num in my_list:
    if num % 2 == 0:
        print(num)



#Part 2: Dictionaries
#1. Create a dictionary of 5 countries and their capitals.
#2. Print the capital of 2 countries.
#3. Add a new country-capital pair.
#4. Change the capital of one country.
#5. Loop through and print all countries and capitals.

my_dict = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Portugal": "Lisbon"
}
print(my_dict["France"])
print(my_dict["Germany"])
my_dict["Netherlands"] = "Amsterdam"
my_dict["Italy"] = "Milan"
for country, capital in my_dict.items():
    print(f"The capital of {country} is {capital}")



#Part 3: Sets
#1. Create a set of your favorite fruits.
#2. Add a new fruit, then remove one.
#3. Create another set of fruits your friend likes.
#4. Print:
#   - Fruits you both like (intersection).
#   - Fruits only you like (difference).
#   - All fruits either of you like (union).

my_fruits = {"apple", "banana", "cherry"}
my_fruits.add("orange")
my_fruits.remove("banana")
friend_fruits = {"banana", "kiwi", "cherry", "mango"}
print("Intersection:", my_fruits.intersection(friend_fruits))
print("Difference", my_fruits.difference(friend_fruits))
print("Union", my_fruits.union(friend_fruits))


#Part 4: Tuples
#1. Create a tuple of 5 colors.
#2. Print the first and last color.
#3. Loop through the tuple and print each color.
#4. Try to change one color (note the error).
my_colors = ("red", "blue", "green", "yellow", "purple")
print(my_colors[0])
print(my_colors[-1])
for color in my_colors:
    print(color)
my_colors[0] = "pink" 
