'''
Let's convert a number grade to a letter grade, using if and elif statements and comparisons.

Have the user enter a number representing the grade (0-100)
Convert the number grade to a letter grade

Numeric Ranges

90-100: A
80-89: B
70-79: C
60-69: D
0-59: F

'''
import random
rival = random.randint(1, 100)


grade = int(input("Please enter a grade percentage: "))

print("")

if grade > 89 and grade < 101:
    print("You scored an A")
elif grade > 79 and grade < 90:
    print("You scored a B")
elif grade > 69 and grade < 80:
    print("You scored a C")
elif grade > 59 and grade < 70:
    print("You scored a D")
elif grade > 100:
    print("Invalid Grade")
else:
    print("You scored an F")

print("")

print(f'This is your rival\'s score: {rival}')

print("")

if grade > rival:
    print("Your score was better than your rival's score!")
else:
    print("Your rival got a better score.")
