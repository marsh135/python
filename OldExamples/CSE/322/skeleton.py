"""
This program is intended as a tracer round for the flow of control as 
a user of a social media account makes, deletes, and edits posts. For 
testing, a user should be able to enter their user name, change which 
user name they are currently using, add a post using their current user 
name, remove a post made under their current user name, edit a post 
made under their current user name, print the contents of the list of 
posts, or quit the program.
"""

# This line of code tells the Python interpreter that it needs to 
# reference the post.py file in order to run the rest of the code 
# in this file.
import Post

# How will you save the posts you will create? Review the for loop 
# near the end of this code for an answer.

all_posts_archive = []

# What is the user name they want to use?
username = input("Please enter a username: ")
print(f"Welcome, {username}")

# Welcome user to the program 
print("Welcome! Please make a selection: ")

# Store initial user input in a variable identified by user_input
# You may need to use this statement again to complete the activity.

user_input = input(""" What would you like to do?
"add" - Add a post to the archive
"remove" - Remove a post from the archive
"change user" - Change the user name associated with any future posts
"print" - Display the current up to date list of all posts
"quit" - End the program

""")

# This while loop ensures that the program will continue executing 
# statements at the next indentation level until the user types "quit" 
# in response to the prompt.
while user_input != "quit":

    # code for adding a post here
    if(user_input == "add"):
        post = input("What would you like to post?: ")
        all_posts_archive.append(post)

    # code for removing a post here
    elif(user_input== "remove"):
        i = int(input("Which item would you like to remove? "))
        if i in range(0, len( all_posts_archive)):
            del  all_posts_archive[i]
        else:
            print("Index out of range")


    # code for changing the current user here
    elif(user_input== "change user"):
        username = input("Please enter a username: ")
        print(f"Welcome, {username}")

    # code to display all posts, you can use the code in comments below
    elif(user_input== "print"):
        print("POSTS:")
        print("~"*25)
        for post in  all_posts_archive:
            print(post); print()
        print("end of posts")
        

    # code to inform the user that their input was not valid here
    else:
        print("your input was invalid")
    
    # code that will allow the user to make a new selection

    user_input = input(""" What would you like to do?
    "add" - Add a post to the archive
    "remove" - Remove a post from the archive
    "change user" - Change the user name associated with any future posts
    "print" - Display the current up to date list of all posts
    "quit" - End the program

    """)

    # This code will finish the loop
    #break