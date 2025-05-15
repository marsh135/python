#shoutout Johnson Chen

def menu(items):
    for i in range(len(items)):
        print(i, items[i])
        
    while(True):
        choice = int(input("Choice?: "))
        if(choice>= 0 and choice<len(items)):
            break
    return choice

done = False
total = 0
orderNum = 1
order = []
while(not done):
    
    sandwiches = ['no', 'chicken', 'beef', 'tofu' ]
    scost = [0, 5.25, 6.25, 5.75]
    drinks = ['no', 'small', 'medium', 'large']
    dcost = [0, 1.00, 1.75, 2.25]
    fries =  ['no', 'small', 'medium', 'large']
    fcost = [0, 1.00, 1.50, 2.00]
    order.append(orderNum)
    print("Choose a sandwich: "); print()
    schoice =  menu(sandwiches)
    print("-"*20)
    print("Choose a drink size: ");print()
    dchoice = menu(drinks)
    print("-"*20)
    print("Choose a fry size: "); print()
    fchoice = menu(fries)
    
    if(schoice !=0):
        print(f"You chose a {sandwiches[schoice]} sandwich. The cost is ${scost[schoice]:.2f}")
        total+=scost[schoice]
        print(f"Your total is ${total:.2f}"); print()
        print()
        order.append(sandwiches[schoice])
    if(dchoice !=0):
        print(f"You chose a {drinks[dchoice]} drink. The cost is ${dcost[dchoice]:.2f}")
        total+=dcost[dchoice]
        print(f"Your total is ${total:.2f}"); print()
        print()
        order.append(drinks[dchoice])
    if(fchoice !=0):
        print(f"You chose a {fries[fchoice]} fry. The cost is ${fcost[fchoice]:.2f}")
        if(fchoice == 1):
            megasize = input("Would you like to megasize your fries? (Y/N)").strip().upper()
            if(megasize == "Y"):
                fchoice == 3
            else:
                fchoice == 1
        total+=fcost[fchoice]
        print(f"Your total is ${total:.2f}"); print()
        print()
        order.append(fries[fchoice])
    #print(f"Your total is ${total:.2f}"); print()
    if(schoice!=0 and dchoice!=0 and fchoice!=0):
        print("-"*20)
        print("You saved $1.00 by ordering a combo meal!");print("-"*20);print()
        total-=1
    print("-"*20)
    kp = int(input("How many ketchup packets would you like?: "))

    total = total + (kp*.25)
    print("-"*20)
    #print(f"Items in order {orderNum}: {order[orderNum+1]} sandwich, {order[orderNum+2]} drink, {order[orderNum+3]} fries, and {order[orderNum+4]} ketchup packets" )
    more = input("Another item? (Y/N)").strip().upper()
    if(more == 'N'):
        done = True
        print();print()
    else:
        orderNum+=1
        

print(f"Thank you for your order. Your total is ${total:.2f}.")
print(f"Items in order:{order}" )
