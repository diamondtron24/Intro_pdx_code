'''
Lab 7: Guess the Number
Let's play 'Guess the Number', the computer will choose a random int between 1 and 10. The user will then try to guess the number, and the program will tell them whether they're right or wrong.

Advanced Version 1
Tell the user whether their guess is above ('too high!') or below ('too low!') the target value.

Advanced Version 2
Let them keep guessing in a while loop. Keep track of how many guesses the user has made, and tell them at the end.

Advanced Version 3
Using a while loop, allow the user to guess 10 times. If they fail to guess the number after 10 tries, the user is told they've lost.

Advanced Version 4 - WORKING ON THIS ONE
Tell the user whether their current guess is closer than their last.

Super Advanced Version 1
Swap the user with the computer: the user will pick a number, and the computer will guess until they get it right.
'''


import random
#computer = random.randint(0, 10)
x = 0
#last_number = 0
while x < 10:
    user_number = int(input("Please select a number between 0, and 10. "))
    computer = 4
    if user_number == computer:
        print(f'The Computer chose {computer} and you chose {user_number} You guessed correctly!')
        x = 10
    else:
        x += 1
#        abs_number = abs(last_number - user_number)
        if user_number < computer:
            print("Your number is lower than the computers number")
            print (f'That number is incorrect, You have made {x} guesses.')
        else:
            print("Your number is higher than the computers number")
            print (f'That number is incorrect, You have made {x} guesses.')
        if x == 10:
            print("Sorry, you guessed too many times, you LOSE")
#        if abs_number < last_number:
#            print("You are closer than your last guess")
#        elif abs_number > last_number:
#            print("You are farther away than your last guess")
#    last_number = user_number
