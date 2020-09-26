import random
import time

userInput = input("Roll Dice? ")

if(userInput.lower() == "yes"):
    print("Grabbing dice...")
    time.sleep(2)
    print("Rolling Dice...")
    time.sleep(2)
    print("Result is: ",random.randint(1,6))
else:
    print("Okay, come back anytime!")
input("Press enter to quit...")
