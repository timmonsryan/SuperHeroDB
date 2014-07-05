import shelve
import os
superherodict = {}

class SuperHero:
#Class for subsequent superheroes
    def __init__(self,name,power_level,domain_type):
        if int(power_level)>10 or int(power_level)<0:
            self.power_level=input('Power Level has to be between 1 and 10.\nChoose again:\n')
        self.power_level=power_level
        self.domain_type=domain_type
        self.name=name

#loads pickle file as dictionary if it exists in dir
superherodict = shelve.open("HeroDBShelve")

def create_superhero():
    #creates instance of SuperHero with attributes inputted by user
    print()
    global superherodict
    name = input("What is the name of this superhero?\n")
    power_level = int(input('\nWhat is %s\'s power level, from 1 to 10?\n'%(name)))
    domain_type = input('\n%s fights in what kind of environment?\n'%(name))
    hero=SuperHero(name,power_level,domain_type)
    superherodict[hero.name] = hero #assigns key:value to dictionary
    return hero

def print_superhero():
    #prints a sentence detailing superhero based on user input
    print()
    key = input('What superhero do you want info on?\n')
    print()
    #prints dict when prompted for info on all heroes
    if key.lower() == 'all':
        for i in superherodict:
            print("{:<20}{:<5}{:<5}".format(i,superherodict[i].power_level,superherodict[i].domain_type))
    #handles incorrect key entry
    elif not key in superherodict:
        print('Hmm, I don\'t think we\'ve defined %s yet.'%(key))
        input('Press \'Enter\' to continue.')
        super_nav_menu()
    else:
        environment_type = (superherodict[key]).domain_type
        article = article_type(environment_type)
        print('%s is a level %s superhero that fights in %s %s environment.'%\
        (key,str((superherodict[key]).power_level),article,environment_type))
        input('Press \'Enter\' to continue.')
    print()
        

def input_mult_heroes():
    #allows users to input mult superheroes to search through
    InputFreq = input("How many superheroes do you want to enter?\n")
    if InputFreq.isdigit() == False:
        print('\nOops.  You have to pick a number here.  Try again.\n')
        input_mult_heroes()
    else:
        InputFreq = int(InputFreq)
    HeroCount = 1
    while int(InputFreq) > 0:
        print()
        print('======================================')
        print('Superhero #%i'%(HeroCount))
        print('======================================')
        create_superhero()
        InputFreq -= 1
        HeroCount += 1

def compare_heroes(hero1,hero2):
    #compares the power levels of two heroes
    powerdiff = abs(int((superherodict[hero1]).power_level) - int((superherodict[hero2]).power_level))
    print()
    if (superherodict[hero1]).power_level > (superherodict[hero2]).power_level:
        powerwin = hero1
        powerlose = hero2
    elif (superherodict[hero2]).power_level > (superherodict[hero1]).power_level:
        powerwin = hero2
        powerlose = hero1
    else:
        print("The skirmish between %s and %s ends in a historic stalemate."%\
              (hero1,hero2))
    print
    if powerdiff in range(1,4):
        print('In a close fight, %s narrowly bests %s.'%(powerwin,powerlose))
    elif powerdiff in range(4,8):
        print('The fight is over in a matter of minutes.  %s beats down %s.'%\
              (powerwin,powerlose))
    elif powerdiff >= 8:
        print('There was no competition.  %s stands over %s\'s mangled figure.'%\
              (powerwin,powerlose))
    input('Press \'Enter\' to continue.')
    

def article_type(word):
    #outputs 'a' or 'an' depending on if the arg string starts with a vowel or not
    WordList=[]
    if word[0].lower() in 'aeiou':
        return 'an'
    return 'a'

def super_nav_menu():
    #displays sentence with keywords that call different methods
    choice = input('\n--------------------\nSuper Hero Nav Menu\n\
--------------------\n[info]\n[compare]\n[add]\n[exit]\n\n')
    if choice == 'info':
        print_superhero()
        super_nav_menu()
    elif choice == 'compare':
        print()
        hero1=input('Who is the first hero we will be comparing?\n')
        print()
        hero2=input('And the second?\n')
        if not hero1 in superherodict:
            print('Hmm, I don\'t think we\'ve defined %s yet.'%(hero1))
            super_nav_menu()
        if not hero2 in superherodict:
            print('Hmm, I don\'t think we\'ve defined %s yet.'%(hero2))
            super_nav_menu()
        compare_heroes(hero1,hero2)
        super_nav_menu()
    elif choice == 'add':
        print()
        input_mult_heroes()
        super_nav_menu()
    elif choice == 'exit':
        on_exit()
    

def on_exit():
    #displays exit message
    filehandler = open("SuperHeroDB.p","w")
    superherodict.close()
    print()
    print('Thank you for looking at my small program, \'Superhero.py\'!')

super_nav_menu()

#messing with adding attributes not previously-defined in __init__
#ignore for now
"""aquaman = SuperHero('Aquaman',9,'water')
aquaman.weapon = 'Trident'
print aquaman.weapon"""

