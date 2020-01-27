import random
import sys

user_Question = input("What question shall you ask the mighty 8 ball? (Press enter to exit) ")
if user_Question == "":
    sys.exit()

responses = ["It is certain", "Without a doubt", "Outlook good", "Yes", "Reply hazy, try again", "Cannot predict now", "My reply is no", "Don't count on it"]
print(random.choice(responses))

input("Press enter to quit...")
