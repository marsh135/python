import time
#CONSTANTS

RED  = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"

def tw(text):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.15) 
tw("PYTHON IS GREATER THAN JAVA")
print()
print(RED+ "THIS IS RED")