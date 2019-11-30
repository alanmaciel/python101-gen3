# Exit the loop correctly using break statement.

# count = 0
# while True:  # this condition cannot possibly be false
#     print(count)
#     count += 1
#     if count >= 5:
#        break                 # exit loop if count >= 5

zoo = ["lion", 'tiger', 'elephant']

while True: 
    animal = zoo.pop()       # extract one element from the list end
    print(animal)
    # if exit loop if animal is 'tiger':
    # if animal == "tiger":
    #     break                # exit loop


# Use == to check if animal is equal to 'elephant'.