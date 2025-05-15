#I think there is no strategy for R-P-S so I planned to choose one of them randomly.

import random

strategy_name = "Choi"


def play_rock_paper_scissors():
    """
    Function to play rock-paper-scissors game 20 times and print the result of each round.
    """
    choices = ['rock', 'paper', 'scissors']
    for _ in range(20):
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

play_rock_paper_scissors()