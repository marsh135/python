'''Our function starts out choosing paper. 
If we win, we stay with paper. If we lose, we change to a random choice
of either rock or scissors.
'''
import random
strategy_name = 'Pulley-Marsh-WinStayLoseShift'

#This is a change



def move(my_history, their_history):
    if len(their_history)==0: #start with paper
       my_move = 'p' 
    elif(their_history[-1] == 'r'):
        my_move = 'p'  
    else:
        my_move = random.choice(['r', 's']) 
    return my_move
    


        
