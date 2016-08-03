"""Write a program able to play the "Guess the number"-game, where the number to be guessed is randomly chosen between 1 and 20. (Source: http://inventwithpython.com) This is how it should work when run in a terminal:

 import guess_number
Hello! What is your name?
Torbjrn
Well, Torbjrn, I am thinking of a number between 1 and 20.
Take a guess.
10
Your guess is too low.
Take a guess.
15
Your guess is too low.
Take a guess.
18
Good job, Torbjrn! You guessed my number in 3 guesses!"""


import random
name = raw_input("Hello! What is your name?\n")
print "Well, %s, I am thinking of a number between 1 and 20." % name
secret = random.randint(1, 20)
i= int(raw_input("Take a guess.\n"))
count = 1
while i!= secret:
   if i< secret:
       print "Your guess is too low."
   elif i> secret:
       print "Your guess is too high."
   i = int(raw_input("Take a guess.\n"))
   count += 1
print "Good job, %s! You guessed my number in %d guesses!" % (name, count)
