sandwiches = ['Chicken', 'Beef', 'Tofu']
prices = [5.25, 6.25, 5.75]
subTotal = 0.00

order = []
while True:
    choice = input('Would you like chicken, beef, or tofu?: ').strip().lower()
    if choice == 'chicken':
        #print('You chose', choice, 'which costs $' + str(prices[0]))
        subTotal+= 5.25
    elif choice == 'beef':
        #print('You chose', choice, 'which costs $' + str(prices[1]))
        subTotal+= 6.25
    elif choice == 'tofu':
        #print('You chose', choice, 'which costs $' + str(prices[2]))
        subTotal+= 5.75
    else:
        print("Your selection is not valid")
        
    bev = input("Would you like a beverage? (Y/N): ").strip().lower()
    if bev == 'y':
        size = input("Would you like a small, medium, or large?: " ).strip().lower()
        if size == 'small':
            #print("A small drink costs $1.00.")
            subTotal = subTotal + 1
        elif size == 'medium':
            #print("A medium drink costs $1.75.")
            subTotal = subTotal + 1.75
        elif size == 'large':
            #print("A large drink costs $2.25.")
            subTotal = subTotal + 2.25
        else:
            print("Invalid.")
    else:
        print("no")

    fries = input("Would you like fries? (Y/N): ").strip().lower()
    if fries == 'y':
        frysize = input("Would you like a small, medium, or large?: " ).strip().lower()
        if frysize == 'small':
            #print("A small fry costs $1.00.")

            mega_fries = input("Would you like to mega-size your fries? (Y/N): ").strip().lower()
            
            if mega_fries == 'y':
                #print("MEGA-SIZE!")
                subTotal = subTotal +2.00
            else:
                subTotal = subTotal + 1

        elif frysize == 'medium':
            #print("A medium fry costs $1.50.")
            subTotal = subTotal + 1.50
        elif frysize == 'large':
            #print("A large fry costs $2.00.")
            subTotal = subTotal + 2.00
        else:
            print("Invalid.")
    else:
        print("no")
    
    ketchup = int(input("How many ketchup packets would you like? (.25 each)"))
    subTotal = subTotal + (ketchup *.25)

    if bev == 'y' and fries =='y':
        subTotal-=1.00
    
    order.append(choice, size, frysize, ketchup)
    print('You ordered a', choice, 'sandwich,', size, "beverage, and", frysize, 'fries, and', str(ketchup), 'ketchup packets.')    
    print(f"Your subtotal is ${subTotal:.2f}.")
