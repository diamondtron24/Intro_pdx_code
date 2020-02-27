'''
Define a list of eyes
Define a list of noses
Define a list of mouths
Randomly pick a set of eyes
Randomly pick a nose
Randomly pick a mouth
Assemble and display the emoticon

Advanced Version 1
Use a for loop to generate 5 emoticons.

Advanced Version 2
In a while loop, ask the user if they want another emoticon

Advanced Version 3
Ask the user if they want to choose each part of the face. If they do,
let the user choose that part of the face. If they don't, randomly generate that
part.

Advanced Version 4
Let the user choose if they want to make one-line horizontal faces like :-),
one-line vertical faces like o_O, or multi-line vertical faces like:
'''

# importing module
import random
'''
Part 1
'''

# Lists

# eyes = [":", ";", "8", ">", "X"]
# noses = ["-", ">", "}", "b", "="]
# mouths = [")", "}", "P", "X"]

# # set face to null
# face = ""
# # question = input("Would you like to Create another emoticon? ")

# eye = random.choice(eyes)
# nose = random.choice(noses)
# mouth = random.choice(mouths)

# face = eye + nose + mouth

# print(face)

'''
Advanced version 1
'''

# Lists
# eyes = [":", ";", "8", ">", "X"]
# noses = ["-", ">", "}", "b", "="]
# mouths = [")", "}", "P", "X"]

# set face to null
# face = ""

# for x in range(5):
#     eye = random.choice(eyes)
#     nose = random.choice(noses)
#     mouth = random.choice(mouths)
#     face = eye + nose + mouth
#     print(face)

'''
Advanced Version 2
'''

# Lists

# eyes = [":", ";", "8", ">", "X"]
# noses = ["-", ">", "}", "b", "="]
# mouths = [")", "}", "P", "X"]
#
#
# another_emoticon = "yes"
#
# while another_emoticon == "yes":
#
#     eye = random.choice(eyes)
#     nose = random.choice(noses)
#     mouth = random.choice(mouths)
#     face = eye + nose + mouth
#     print(face)
#
#     another_emoticon = input("do you want another emoticon?")
#
# else:
#     print("Goodbye")

'''
Advanced version with while True loop
'''

# Lists

# eyes = [":", ";", "8", ">", "X"]
# noses = ["-", ">", "}", "b", "="]
# mouths = [")", "}", "P", "X"]
#
#
#
# while True:
#     eye = random.choice(eyes)
#     nose = random.choice(noses)
#     mouth = random.choice(mouths)
#     face = eye + nose + mouth
#     print(face)
#     another_emoticon = input("do you want another emoticon?")
#     if another_emoticon == "no":
#         break
