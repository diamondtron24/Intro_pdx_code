'''
Lab 10: Anagram Checker
Let's write an anagram checker.

Anagram
Two words are anagrams of each other if the letters of one can be rearranged to fit the other. e.g. dormitory and dirty room.

Write a program that lets the user enter two strings, and tells them if they are anagrams of each other.

Convert the strings into lists (list)
Sort the letters of each word (sort)
Check if the two are equal
>>> enter the first word: dormitory
>>> enter the second word: dirtyroom
>>> 'dormitory' and 'dirtyroom' are anagrams

Advanced Version 1
Convert each word to lower case (lower)
Remove all the spaces from each word by replacing them with empty strings (replace)

Advanced Version 2 - DONE
Make your program ignore punctuation when checking anagrams.

Advanced Version 3
Let the user enter as many words as they choose. If every word is an anagram of every other word, let the user know.
'''

import string

print("Lets play Anagram Checker!")
string1 = input("Please enter string 1: ").lower().replace(" ", "")
string2 = input("Now enter string 2: ").lower().replace(" ", "")

# This converts the strings into a List
list1 = list(string1)
for item in list1:
    if item in string.punctuation + " ":
        list1.pop(list1.index(item))
list2 = list(string2)
for item in list2:
    if item in string.punctuation + " ":
        list2.pop(list1.index(item))
# this sort the lists alphebetically then saves it to a string (non destructive/imutable )
sort1 = sorted(list1)
sort2 = sorted(list2)

# this prints the original values of list1 and list2
print("list 1 and list 2")
print(list1)
print(list2)


# This takes the old value and sorts it. destrutive/mutable. Old value is replaced
list1.sort()
list2.sort()

# This prints the new value of list1 and list2
print("sort function list 1 and list 2")
print(list1)
print(list2)

if list1 == list2:
    print(f'{string1} and {string2} are anagrams')
else:
    print(f'{string1} and {string2} are NOT anagrams')
