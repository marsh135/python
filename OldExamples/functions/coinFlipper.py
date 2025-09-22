import random
import matplotlib.pyplot as plt #graph
import numpy as np #graph

flips = int(input("Please enter a number of flips: "))
           
def flipper(flips):
    
    heads = 0
    tails = 0
    for number in range(flips):
        result = random.randint(0,1)
        if result ==0:
            print("Heads")
            heads +=1
        else:
            print("Tails!")
            tails +=1
    print("Heads: " + str(heads) + "   Tails: " + str(tails))
    graph = np.array([heads, tails]) #graph
    plt.pie(graph)#graph
    plt.show()#graph

flipper(flips)








