'''
Lab 8: Password Generator
Let's generate a password ten characters long using a loop (while loop or for loop) and random.choice, this will be a string of random characters.

Advanced Version 1
Allow the user to choose how many characters the password will be.

Advanced Version 2
Allow the user to choose how many letters, numbers, and punctuation characters they want in their password. Mix everything up using list(), random.shuffle(), and ''.join().
'''

import random
import string

password_character = string.ascii_letters
all_characters = string.ascii_letters + string.digits + string.punctuation

one = ""
new_value = ""

password_length = int(input("How many characters would you like your password to be? "))

x = 0
while x < password_length:
    one = random.choice(all_characters)
    new_value += one
    x += 1
print(f'Your new password is: {new_value}')
