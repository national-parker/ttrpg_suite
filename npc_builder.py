#Nat'l Parks' NPC generator
#this was programed in python 3.9.4
'''this NPC generator is meant to help with quick NPC generation, putting out a
couple of NPCs with description and characteristics, not stats aside
from a high stat/low stat for physical description.'''
#motivations tbd

'''core archetecture is going to be basic:
Program will deliver a dictionary, then print using key:item pairings.'''

from random import randint
from lib.asset_helper import rand_asset_line  #this function was built to take a .txt file as its argument
from lib.asset_helper import pick_one_from_list  #this function takes a list as its argument
from lib.asset_helper import choose_ancestry  #this function takes a directory as its argument; read file for percentage breakdown

#for the high stat/low stat system
stats = ['strength','dexterity','constitution','intelligence','wisdom','charisma']

#function to pick a high stat and low stat
def high_low(char):  #will take a dictionary, return a 'h_stat' and 'l_stat' key:item pairing
    char['h_stat'] = pick_one_from_list(stats)
    char['l_stat'] = pick_one_from_list(stats)
    z = 0  #a break command to ensure the while loop doesn't lead to a crash
    while char['h_stat'] == char['l_stat']:  #use a while loop to repeat the choice until a different result
        char['l_stat'] = pick_one_from_list(stats)
        z += 1
        if z > 100:
            break
    #print(char['h_stat'] ,char['l_stat'])
    return char

#okay, this last bit will be the part to build out an NPC using the other lists
def choose_pronouns(char):  #2021 UCLA Williams Inst. study found approx. 1.2 million nonbinary Americans, majority under 29 and white = 0.36% US pop
    x = randint(1,100)
    if x <= 50:  #assuming greater proportion of women than men
        char["pronoun"] = "she"
    elif x <= 99:  #bumping non-binary pronoun use to 1%, can revisit later
        char["pronoun"] = "he"
    else:
        char["pronoun"] = "they"
    return char

def build_npc():  #creates and returns a dictionary
    character = {}
    choose_ancestry(character)  #calls the choose_ancestry function which adds ancestry to the dictionary
    character['job, city'] = rand_asset_line('assets/jobs_city.txt')  #call the rand_asset_line function on the jobs_city file
    character['job, rural'] = rand_asset_line('assets/jobs_rural.txt')  #call the rand_asset_line function on the jobs_city file
    character['apperance'] = rand_asset_line('assets/general_appearance.txt')  #call the rand_asset_line function on the jobs_city file
    character['physical trait'] = rand_asset_line('assets/distinctive_trait.txt')  #call the rand_asset_line function on the jobs_city file
    character['personality'] = rand_asset_line('assets/personalities.txt')  #call the rand_asset_line function on the jobs_city file
    choose_pronouns(character)
    high_low(character)
    return character

#okay, let's add the vowel-checker to make the first line of into_plaintext() below look good, and could/should I add a gender poriton while at it?
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

def describe(char):  #this program will print out a nice sheet for the NPC, taking the directory built above as its argument
    print('')
    if char['apperance'][0] in vowels:  #appearance, ancestry, physical traits
        print("This npc is an %s %s with %s and a %s personality." % (char["apperance"], char["ancestry"], char["physical trait"], char['personality']))
    else:
        print("This npc is a %s %s with %s and a %s personality." % (char["apperance"], char["ancestry"], char["physical trait"], char['personality']))
    if char['pronoun'] == 'they':  #job
        print("If they are encountered in a city, they are a %s.  Otherwise, they are a %s." % (char["job, city"], char["job, rural"]))
    else:
        print("If %s lives in a city, %s is a %s.  Otherwise, %s is a %s." % \
              (char["pronoun"], char["pronoun"], char["job, city"], char["pronoun"], char["job, rural"]))
    print("High stat: %s      Low stat: %s" % (char["h_stat"],char["l_stat"]))

'''#quickly testing by building 3 NPCs
for i in range(3):
    describe(build_npc())'''

#this is the variable output setting
print("welcome to national parks' random npc generator")
valid_input = False 
while not valid_input:
    x = input("How many npcs would you like to generate?  ")
    if x.isdigit():  #checks that each character in the string is a number
        x = int(x)  #converts the number to an integer (which it should already be)
        x = min(10,x)  #makes x the smaller of itself and 10, i.e. reduces large numbers
        x = max(1, x)  #makes x the larger of itselff and 1, i.e. no 0
        for i in range(x):
            describe(build_npc())
        valid_input = True
    else:
        print("invalid entry, please try again")
        print('')

