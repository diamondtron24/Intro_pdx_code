# Create a List

Stuff = []
# This is how to create a List

fruits = ['apples', 'oranges', 'grapes', 'pears']
# exmaple of a list
print fruits

# Get the value

print("fruits")

# Get the value

print fruits([2])

# Get the length

print(len(fruits))

# Add to the List

fruits.append("cherry")
print(fruits)

# remove from a List
fruits.remove("oranges")
print(fruits)

#Insert into a position
fruits.insert(3, "banana")
print fruits

#Remove from a position
fruits.pop(-1)
# -1 removes the last item in a list

print fruits

# Loop though the elements of a List

for tiger in fruits:
print(f"{tiger} has an index of {fruits.index(tiger)}")

#Loop though the indexes of a List

for i in range(2):
    print(fruits[i])
