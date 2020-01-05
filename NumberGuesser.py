import random

userNumber = input("Pick a number from 1-10:")

CPUNumber = random.randint(1,1)

if(int(userNumber) == CPUNumber):
    print("You've guessed correctly!")
elif(int(userNumber) != CPUNumber):
    print("You've guessed incorrectly!")
input("Press enter to quit...")
