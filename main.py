pages = input("How many pages do you have to read? ")
time = input("In how many days do you have to read the book? ")

total = int(pages) // int(time)
print("You will have to read " + str(total) + " pages per day to finish in " + str(time) + " days." )

input("Press enter to quit...")