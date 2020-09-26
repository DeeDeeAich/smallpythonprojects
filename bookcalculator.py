pages = input("How many pages do you have to read? ")
time = input("In how many days do you have to read the book? ")

total = int(pages) // int(time)
print(f"You will have to read {total} pages per day in order to finish in {time} days.")

input("Press enter to quit...")
