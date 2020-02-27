


import string
import random
letters = string.ascii_letters
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
print(string.digits)
print(string.punctuation)
all_characters = string.ascii_letters + string.digits + string.punctuation
print(random.choice(all_characters))
print(f"All letters: {letters}")
print(f"All lowercase: {lowercase}")
print(f"All uppercase: {uppercase}")

password = ""
# For loop using a range. 
for i in range(5):
    password += "a"
print(password)
for i in range(5):
    print("a", end="")
print()
