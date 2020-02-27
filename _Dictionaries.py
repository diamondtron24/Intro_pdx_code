
wings = {
    "buffalo": 4,
    "habanero": 8,
    "ghost": 10,
    "mild buff": 2,
    "teriyaki": 1,
    "garlic parm": 1,
    "spicy bbq": 3,
}

print(wings)
print(wings["garlic parm"])

total = 0
for sauce in wings:
    total += wings[sauce]
# this will print the total of the wings dictionary (29)
print(total)
# this will print the average number for the wings dictionary (4.14x)
print(total/len(wings))

#this adds a new sauce to the dictionary with user input
new_sauce = input("enter a new sauce : ")
heat = input("Enter the hotness: ")

wings[new_sauce] = heat

print(wings)

pop removes an item from the dictionary
remove = input("what sauce would you like to remove? ")
wings.pop(remove)
print(wings)
# remove an item with a message if item not found
remove = input("what sauce would you like to remove? ")
print(wings.get(remove, "Not found"))

# keys and values in dictionaries
keys = wings.keys()
values = wings.values()
print(keys)
print(values)
print(wings.get("tomato", "Not found"))
