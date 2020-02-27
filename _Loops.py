# For Loop

# list1 = ["apples", "cherries", "pears"]

# for i in range(1, 3,):
#    print("Hello")



# While Loops

'''
x = 0
while x < 5:
    print("Hello")
    print(x)
    x += 1
'''


y = 0
while y < 4:
    y += 1
    if y == 2:
        print("This is our 2 Continue point")
        continue
    print(y)


# Class stuff:

list1 = ["apples", "cherries", "pears"]
#
# for i in range(2):
#     print("hello")
students = [
    "Allyson",
    "Andrew",
    "Christopher",
    "Jai",
    "Jasmine",
    "Jonathan",
    "Marquis",
    "Nick",
    "RaSharde",
    "Steve",
]
#
# for item in list1:
#     print(item)
# for person in students:
#     print(f"Hello {person}")
x = 7
while x < 5:
    print(x)
    if x == 3:
        break
    x += 1
y = 8
while y < 4:
    y += 1
    if y == 2:
        print("hello")
        continue
    print(y)
y = 8
while y > 4:
    print(students[y])
    y -= 1
    if y == 6:
        break
else:
    print("Hi")
