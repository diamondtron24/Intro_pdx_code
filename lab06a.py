'''
Lab 6: Rock Paper Scissors
Let's play rock-paper-scissors with the computer.

The computer will ask the user for their choice (rock, paper, scissors)
The computer will randomly choose rock, paper or scissors
Determine who won and tell the user
Let's list all the cases:

rock vs rock (tie)
rock vs paper
rock vs scissors
paper vs rock
paper vs paper
paper vs scissors
scissors vs rock
scissors vs paper
scissors vs scissors
Advanced Version 1
Catch all tie conditions using a single if conditional.

Advanced Version 2
Ask the user if they want to play again, using a while loop.

Advanced Version 3
Use a dictionary where each key is one of the choices, and the value associated with the key is a list containing the two other choices.
'''

import random

# Lab 6

# list
items = ["rock", "paper", "scissors"]

print("Let/'s play Rock, Paper, Scissors!")

# variables
user = input("Rock, Paper or Scissors? ").lower()
computer = random.choice(items)

if user == computer:
    print("It\'s a Tie")
print(f'Computer chooses: {computer}')
if user == "rock":
    if computer == "scissors":
        print("User Wins!")
    else:
        print("Computer Wins")
if user == "paper":
    if computer == "rock":
        print("User Wins!")
    else:
        print("Computer Wins")
if user == "scissors":
    if computer == "paper":
        print("User Wins!")
    else:
        print("Computer Wins")
