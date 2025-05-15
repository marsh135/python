from Post import Post

all_posts_archive = []
print()
print("Posting Software")
print()
username = input("Please enter a username: ")
print()
print(f"Welcome, {username}")
print("~"*25);print()
print("Make a selection: add, remove, change user, print, help, quit")

print()
user_input = input("Your response:")

while user_input != "quit":
    # code for adding a post here
    if(user_input == "add"):
        message = input("What would you like to post?: ")
        post = Post(username, message)
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
            #index+=1
        print("end of posts")
    
    elif(user_input == "help"):
        print("The following options are available:")
        print("add - Add a post to the archive")
        print("remove - Remove a post from the archive")
        print("change user - Change the user name associated with any future posts")
        print("print - Display the current up to date list of all posts")
        print("quit - End the program")

    # code to inform the user that their input was not valid here
    else:
        print("your input was invalid")
    
    # code that will allow the user to make a new selection

    print("~"*25);print()
    print("Make a selection: add, remove, change user, print, help, quit")
    print()
    user_input = input("Your response: ")

    # This code will finish the loop
    #break