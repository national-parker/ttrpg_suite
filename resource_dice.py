#running tests to see how long it takes to deplete resource dice
#plan is to use a while loop, running while dice remain, and to do 10 (then 10,000 iterations) to see the outcomes

from random import randint  #for dice rolling
from decimal import Decimal  #to truncate at the end
import statistics  #for mean, median, and mode


'''WARNING: if you're going to enable any of the debugging below to show results mid-loop, make sure you reduce the numberoftests value to something smaller/more legible'''
numberoftests = 100001  #see VARIABLE INPUT SECTION below; the number of overall tests; keeping to 100k for my poor laptop


#MAIN FUNCTION SECTION
def supply_dice(ndice, ntests):  #will take two arguments: the number of supply dice and the number of tests to run it on
    finallist = []  #will be the output list to run statistical tests on
    for r in range(ntests):  #will loop a number of times equal to the test variable
        diceremaining = ndice  #set the dice remaining for this given loop equal to the number of supply dice
        someremain = True  #set up for a while loop: will check if there are dice remaining at the end of the while loop and end the loop when none left
        nrolls = 0  #start a tally for how many times through the while loop we go
        while someremain:  #see id
            nrolls += 1  #add one for each roll
            rolls = []  #create an empty list for the rolls to go into
            for i in range(diceremaining):  #will roll a number of six sided dice equal to the number of supply dice and add them to the list for this while loop
                rolls.append(randint(1,6))  #see id
            lost = rolls.count(1)  #count how many dice rolled a "1", indicating that supply dice is lost
            diceremaining -= lost  #subtract the lost dice from the dice remaining

#debugging (apostrophe comment the next three lines out for final)
            '''print(rolls)  #show what the rolls were each iteration of the while loop
            print("lost: " + str(lost))  #confirm how many of above were 1
            print("remaining: " + str(diceremaining))  #confirm how many supply dice should be left'''
#end of debugging
            
            if diceremaining == 0:  #close the while loop once the last supply dice is lost
                someremain = False

#more debugging
        '''print("TOTAL ROLLS: " + str(nrolls))  #should show us how many rolls and how many times through the
        print("")  #to skip a line'''
#end of more debugging
        
        finallist.append(nrolls)  #add how many rolls it took to the output list for statistical analysis

#last debugging        
    #print(finallist)  #show the list of how many rolls it took
#end of last debugging

    #get the mean to two decimal places
    meanforoutput = Decimal(statistics.mean(finallist))  #making the mean a Decimal for the truncation function to run
    tmeanforoutput = meanforoutput.quantize(Decimal('1.000'))  #truncating the mean to three decimal places

    print("")
    print("MEAN NUMBER OF ROLLS TO ZERO:   " + str(tmeanforoutput))
    print("MEDIAN NUMBER OF ROLLS TO ZERO: " + str(statistics.median(finallist)))
    print("MODE NUMBER OF ROLLS TO ZERO:   " + str(statistics.mode(finallist)))


#VARIALBE INPUT SECTION
print("welcome to national parks' supply dice statistical analysis module")
print(" a brute-force solution to forgetting your AP Stats class!")
print("")

valid_input = False  #will check that the input works for this function
z = 0  #safety escape from the below while loop

while not valid_input:
    x = input("How many supply dice would you like to check?  ")

    if x.isdigit():  #checks that each character in the string is a number
        x = int(x)  #converts the number to an integer (which it should already be)
        x = min(10,x)  #makes x the smaller of itself and 10, i.e. reduces large numbers
        x = max(1, x)  #makes x the larger of itselff and 1, i.e. no 0

        supply_dice(x, numberoftests)  #calls the supply dice function and runs it through the set number of trials (defined in first rows)

        valid_input = True  #the input was valid

    else:  #if the input isn't valid--gives them another chance
        z +=1
        if z > 2:
            break
        print("invalid entry, please try again")
        print('')

            


#showing my work, these were the tests and examples used to build above:

#how to use statistics tools examples/testing
'''data = [1, 2, 2, 3, 5, 8, 9, 15]
mean_value = statistics.mean(data)
print(mean_value)

median_value = statistics.median(data)
print(median_value)

mode_value = statistics.mode(data)
print(mode_value)'''

#testing dice rolling basics
'''def average_randoms(runs):
    for r in range(runs):
        r_data = []
        for i in range(5000):
            r_data.append(randint(0,10))
        #r_data.sort()
        #print(r_data)
        print(statistics.mean(r_data))
average_randoms(10)'''
