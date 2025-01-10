'''
COIN TOSS PROGRAM
(GUESSING HEADS OR TAILS)
'''

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

'''
======================================================================================================
SIMPLIFIED SQUARE ROOT FINDER
'''

def Ave(m,n):   #averages two numbers
     v = (m+n) / 2.0
     return v
def SqRt(n):   #will print the square root of number "n"
    lo = 0.0   #setting the lower bound
    hi = n   #setting the upper bound
    mi = Ave(lo,hi)   #setting the middle value
    c = 0   #setting the cycle counter
    while(abs(mi**2-n)>0.0000001):   #loop terminates when the middle number squared is within one ten-millionth of the goal number
    #for _ in range(100):   #for loop for proof of concept before putting in while loop
        Ln = Ave(lo,mi)   #lower average to test
        Un = Ave(mi,hi)   #upper average to test
        if abs(Ln**2-n) < abs(Un**2-n):   #the Ln is closer to the square root, so lower the upper bound
             hi = mi   #lowering the upper bound
             mi = Ave(lo,hi)   #setting the new midpoint
        else:   #the Un must be closer, so raise the lower bound
             lo = mi   #raising the lower bound
             mi = Ave(lo,hi)   #setting the new midpoint
        #print mi   #debugging print command
        c += 1   #raising the cycle counter
    print c   #printing the number of cycles taken
    print mi   #printing the square root

'''
Run function by:

SqRt( number )   #testing the function
'''
