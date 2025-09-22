# RP, DM, MH
# 12/5/23

import random
import psrock
import its_late

strategy_name = "Alternate Between Paper Scissor and Rock"
count = 0


def move(my_history, their_history):
    lister = ["r", "s", "p"]
    lister2 = ["p", "r", "s"]
    its_late.count += 1

    number = random.randint(1, 2)
    if number == 1:
        return lister[its_late.count % 3]
    elif number == 2:
        return lister2[its_late.count % 3]


