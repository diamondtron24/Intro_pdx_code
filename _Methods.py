'''
Pick 3 string methods and list methods
demonstrate how they work.
'''

# center function
text1 = "This is the center string method."

run_test = text1.center(50)
# should return
#        This is the center string method.
print(run_test)

# Format function
text2 = "This is this a test for the format method, I made {money} dollars!"
# should return "This is this a test for the format method, I made 34567 dollars!"
print(text2.format(money = 34567))

# islower function
x = "this is a test of the islower function."
y = "This is a test of the islower function"

text3 = x.islower()
text4 = y.islower()

# return true
print(text3)
# return false
print(text4)

# append to list1
list1 = [1, 2, 3]
# This should add 4 to list1
list1.append(4)
# should print [1, 2, 3, 4]
print(list1)

# copy function

list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

x = list2.copy()
# This should print [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(x)

# index methods

list3 = [1, 2, 3, 4, 5, 6]
x = list3.index(5)
# This should print 4
print(x)
