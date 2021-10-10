'''this holds the function to pick a random line in a text file, then
return the line cleaned up of its last character (i.e. no new line
character'''

from random import randint

def rand_asset_line(file_path_to_asset):  #defining the function, which will take a text file as its argument
    with open(file_path_to_asset) as asset:  #opens the text file
        x = asset.readlines()  #create list with each line as separate item
        i = randint(0 , len(x)-1)  #pick random number within the length of the list
        result = x[i]  #result is the string chosen by random number
        result = result[:-1]  #should return the whole of result except the last index
        return result

def pick_one_from_list(chosen_list):  #this program will iterate within a given list and pick a random one
    y = randint(1,len(chosen_list))
    return chosen_list[y-1]  #return the item at index y-1 in the list        

'''ancestry uses a percentile system between common, uncommon, and rare ancestries
rarity is based on my homebrew world, with the following percentages:
35% human, 35% common, 20% uncommon, and 10% rare.
feel free to customise to your setting if desired'''

def choose_ancestry(char):  #this function will call rand_asset_line()
    x = randint(1,100)  #set x which determines the rarity of the race
    if x <= 35:  #if x is in the 1-35 range, call rand_asset_line() with 
        char["ancestry"] = rand_asset_line('assets/ancestries_human.txt') #use the above function, but will return human
    elif x <= 70:  #if x is in the 36-70 range
        char["ancestry"] = rand_asset_line('assets/ancestries_common.txt')
    elif x <= 90:  #if x is in the 71-90 range
        char["ancestry"] = rand_asset_line('assets/ancestries_uncommon.txt')
    else:  #for all other situations, which is 91-100 range
        char["ancestry"] = rand_asset_line('assets/ancestries_rare.txt')
    return char

def rolling4d6dropLowest(l):  #funciton accepting argument l which will be an empty list
    for i in range(6):  #a for loop which will run 6 times, once for each final stat
        n = []  #forming empty list which randint will append d6 rolls into to simulate the four rolls
        for j in range(4):
            n.append(randint(1,6))  #rolling the four d6
        n.sort()  #sorting them low-high
        del(n[0])  #dropping the lowest
        score = sum(n[0:])  #adding up the remaining three
        l.append(score)  #adding each score to the list taken as argument for the function
    l.sort(reverse=True)  #sorting the list taken as argument for the function from high-low
    return l  #returning the list with the six scores
