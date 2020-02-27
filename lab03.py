'''
Magic 8 Ball answers

It is certain.
It is decidedly so.
Without a doubt.
Yes - definitely.
You may rely on it.
As I see it, yes.
Most likely.
Outlook good.
Yes.
Signs point to yes.
Reply hazy, try again.
Ask again later.
Better not tell you now.
Cannot predict now.
Concentrate and ask again.
Don't count on it.
My reply is no.
My sources say no.
Outlook not so good.
Very doubtful
'''
import random

answer = ['It is certain.',
'It is decidedly so.',
'Without a doubt.',
'Yes - definitely.',
'You may rely on it.',
'As I see it, yes.',
'Most likely.',
'Outlook good.',
'Yes.',
'Signs point to yes.',
'Reply hazy, try again.',
'Ask again later.',
'Better not tell you now.',
'Cannot predict now.',
'Concentrate and ask again.',
'Don\'t count on it.',
'My reply is no.',
'My sources say no.',
'Outlook not so good.',
'Very doubtful']

#Answer = input("Would you like to ask another question? ")

#for i in range(2):
print("Welcome to your Magic * ball")
print("")

question = input("Please ask your Magic 8 Ball a question: ")
print("")
print(f'Your question was, {question}')
print("")
print(random.choice(answer))
print("")
    #print(answer)
