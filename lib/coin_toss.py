#get the randint function
from random import randint

#use it to determine heads (0) or tails (1) and set the invalid input response
coin = randint(0, 1)
if coin == 0:
    c = "heads."
if coin ==1:
    c = "tails."
invir = "Invalid input, please choose heads or tails."

#DEBUG, print what it is
##print c

#get the player's guess
guess = raw_input("Call it, heads or tails: ")

#check to make sure they put in letters, and make them lowercase
if len(guess) > 0 and guess.isalpha():

#turn the guess into a number by checking first letter h will be 0 and t will be 1, if neither, it'll go to 2
    guess = guess.lower()
    if guess[0] == 'h':
        gue = 0
    elif guess[0] == 't':
        gue = 1
    else:
        gue = 2
        print invir
else: 
    gue = 2
    print invir

#adding a line break for beauty
print " "

#if gue is coin, win, otherwise loss
if gue == coin:
    print "Correct!"
else:
    print "Sorry, you guessed incorrectly. It was actually " + c

print " "

