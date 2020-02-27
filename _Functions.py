def print_list(my_list):
    print(my_list)

music = ["hip hop", "rock", "pop", "jazz", "country"]

print_list(music)

def print_list(my_list):
    # This variable will be set so each element prints on its own line
    for element in my_list:
        print(element)

music = ["hip hop", "rock", "pop", "jazz", "country"]
drinks = ["vodka", "gin", "whiskey"]
'''
Should print this way:
hip hop
rock
pop
jazz
country
vodka
gin
whiskey
'''
print_list(music)
print_list(drinks)

import random

def grade(score):

    if 90 <= score <= 100:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    elif 60 <= score <= 69:
        return "D"
    else:
        return "F"



score = int(input("Enter your score: "))
rival = random.randint(0, 100)

score = grade(score)
rival = grade(rival)

print(f"You got a {score}")
print(f"This loser got a {rival}")


def gravity(user):
    if user == "yes":
        return
    elif user == "no":
        print("Hi there")
user = input("yes or no")
gravity(user)
