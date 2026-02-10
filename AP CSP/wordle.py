import random
GREEN = "\033[1;42m\033[1;30m"  # bold black text on green background
YELLOW = "\033[1;43m\033[1;30m" # bold black text on yellow background
GRAY = "\033[1;100m\033[1;37m"  # bold white text on dark gray background
RESET = "\033[0m"

WORDS = ["apple", "bench", "crane", "doubt", "eagle", "flame", "grace", "house",
    "input", "jolly", "karma", "linen", "mango", "noble", "ocean", "piano",
    "query", "round", "shine", "tiger", "union", "vivid", "woven", "xenon",
    "young", "zesty"]
secret = random.choice(WORDS)
MAX_GUESSES = 6
WORD_LEN = 5

print("Wordle!")
for attempt in range(1, MAX_GUESSES + 1):
    guess = input(f"Guess {attempt}/{MAX_GUESSES}: ").lower()
    if len(guess) != WORD_LEN:
        print(f"Enter exactly {WORD_LEN} letters.")
        continue

    # Evaluate guess
    output = ""
    for i in range(WORD_LEN):
        if guess[i] == secret[i]:
            output += GREEN + guess[i].upper() + RESET # correct place
        elif guess[i] in secret:
            output += YELLOW +guess[i] + RESET  # in word, wrong place
        else:
            output += GRAY + "_" + RESET # not in word
    print(output)

    if guess == secret:
        print(f" Correct! The word was '{secret}'")
        break
else:
    print(f"Out of guesses. The word was '{secret}'")