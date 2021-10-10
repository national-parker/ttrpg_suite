#this was coded in python 3.9.4
'''This is the character builder, it works by creating a directory which it populates
with the character's ancestry (or in 5e language "race"), background, class, and a set
of rolled ability scores. I'm working on how it reminds of ability score increases from
ancestry, but given the derth of non +2/+1 options, we'll see how it plays out.'''

from random import randint
from lib.asset_helper import rand_asset_line  #this function was built to take a .txt file as its argument
from lib.asset_helper import pick_one_from_list  #this function takes a list as its argument
from lib.asset_helper import rolling4d6dropLowest  #this function takes an empty list as its argument
from lib.asset_helper import choose_ancestry  #this function takes a directory as its argument; read file for percentage breakdown

vowels = ['A','E','I','O','U','a','e','i','o','u']  #for the a/an disambiguation for backgrounds

def build_char():  
    character = {"stats" : []}  #starting with almost empty dictionary for character, empty list where stats will be
    rolling4d6dropLowest(character["stats"])  #call each function to build out the character directory
    character['class'] = rand_asset_line('assets/pc_classes.txt')  #call the rand_asset_line function on the pc classes file and return one as the item paired to the 'class' key in dictionary
    character['background'] = rand_asset_line('assets/background.txt')  #does the same, but with backgrounds
    choose_ancestry(character)  #calls the choose_ancestry function which adds ancestry to the dictionary
    return character

def describe(character):  #now for the final print, including a/an
    if character['ancestry'][0] in vowels:
        print("you have rolled an %s %s" % (character['ancestry'], character['class']))  #if ancestry starts with a vowel
    else:
        print("you have rolled a %s %s" % (character['ancestry'], character['class']))  #otherwise
    if character['background'][0] in vowels:  #for a/an check
        print("your character was an %s before adventuring" % (character['background']).lower())  #background list is capatalized, so lower to fix
    else:
        print("your character was a %s before adventuring" % (character['background']).lower())  #background list is capatalized, so lower to fix
    print("your ability scores are: %s" % (character['stats']))
    if character['ancestry'] == 'human':  #presuming no variant human
        print("don\'t forget your score increases: +1 to all")
    else:  #if it's not variant human
        print("don\'t forget your score increases: likely +2/+1") #after done with backgrounds, set to check human, half-elf, etc.
    print("")

#this is the variable output setting
print("welcome to national parks' random character generator")
valid_input = False 
while not valid_input:
    x = input("How many characters would you like to build?  ")
    print('')
    if x.isdigit():  #checks that each character in the string is a number
        x = int(x)  #converts the number to an integer (which it should already be)
        x = min(10,x)  #makes x the smaller of itself and 10, i.e. reduces large numbers
        x = max(1, x)  #makes x the larger of itselff and 1, i.e. no 0
        for i in range(x):
            describe(build_char())
        valid_input = True
    else:
        print("invalid entry, please try again")
        print('')
