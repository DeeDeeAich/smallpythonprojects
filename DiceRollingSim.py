'''
import random
import time

userInput = input("Roll Dice? ")

if(userInput == "Yes" or userInput == "yes" or userInput == "YEs" or userInput == "YES" or userInput == "yEs" or userInput == "yES"):
    print("Grabbing dice...")
    time.sleep(2)
    print("Rolling Dice...")
    time.sleep(2)
    print("Result is: ",random.randint(1,6))
else:
    print("Okay, come back anytime!")
'''

import random
import time

userAnswer = input("Would you like to roll the dice?")

if(userAnswer == "yes"):
    print("Grabbing dice...")
    time.sleep(1.25)
    print("You got a " + str(random.randint(1,6)))
else:
    print("Ok. Come back anytime!")
