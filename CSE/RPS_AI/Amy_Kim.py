"""appeared most random started with rock so we made our first move paper and then random choices after that"""

import random

strategy_name = "Paper first, then random"
                     
                     
def move(my_history, their_history):
      if (len(my_history) == 0):
        my_move = 'p'
        return my_move
      else:
        pick = random.choice(["r", "p", "s"])
        return pick