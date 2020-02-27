'''
lab02

Instructions
Search the interwebs for an example Mad Lib
Create a new file and save it as madlib.py
Ask the user for each word you'll put in your Mad Lib
Use an fstring to put each word into the Mad Lib
'''
print(" ")
print("Let's play a MadLib!")
plural_noun1 = input("Enter a Plural noun: " )
plural_noun2 = input("Enter a second Plural noun: ")
verb1 = input("Enter a Verb: ")
noun1 = input("Enter a noun: ")
verb2 = input("enter a second Verb: ")
plural_noun3 = input("Enter a 3rd Plural noun: ")
noun2 = input("Enter a second noun: ")
plural_noun4 = input("Enter a 4th Plural noun: ")

print(" ")

print(f"""When I go to the arcade with my {plural_noun1}
there are lots of games to play. I spend lots of time there with
my friends. In "Xmen" you can be different {plural_noun2}.
The point of the game is to {verb1} every
robot. You also need to save people, and then you can go to the
next level. In "Star Wars" you are Luke Skywalker and you try to
destroy every {noun1} . In a car racing / motorcycle
racing game you need to beat every computerized vehicle that
you are {verb2}ing against. There are a whole
lot of other cool games. When you play some games you win
{plural_noun3} for certain scores. Once you're done
you can cash in your tickets to get a big {noun2}. You can
save your {plural_noun4} for another time. When I
went to this arcade I didn't believe how much fun it would be.
You might annoy your parents by asking them over and over if
you can go back to there. So far I have had a lot of fun every
time I've been to this great arcade!""")

print(" ")
