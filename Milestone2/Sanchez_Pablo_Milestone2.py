# Pablo Sanchez
# python 2.7.16
# Milestone 2: There Can Be Only One!

'''This is a typical Paper, Rock, Scissors game, 
that is played using Dodge, Parry, Thrust instead.
Dodge beats Parry > Parry beats Thrust > Thrust beats Dodge'''

# Import the random Module
import random

# Here are your list of Pirates
pirates = [
    'Captain William Kidd',
    'Pierre Le Grand',
    'Red Leg Grieves',
    'Edward Low',
    'Calico Jack Rackham',
    'Anne Bonny',
    'Captain Henry Morgan',
    'Black Sam Bellamy',
    'Black Bart Roberts',
    'Edward Blackbeard Teach']

print ("The Pirates are: " + str(pirates))

#  Attacks List
attack = ['dodge', 'parry', 'thrust']

print ("Pirates can use the following Attacks: " + str(attack))

# Choosing the Characters for the fight
player = random.choice(pirates)
opponent = random.choice(pirates)

print "Ahoy ye swabs! Prepare for battle!"
print "The Player ("+ player + ") has challenged the Opponent (" + opponent + ") in one on one combat!\n"

# Game Results

ps = 0
os = 0
game = False

while game == False:
    if ps >= 3 or os >= 3:
        print "Game Over!"
        print "Final Score is: \n" 
        print player + " = " + str(ps)
        print opponent + " = " + str(os)
        game = True
        break

     

#  Choosing the Attack
    pattack = random.choice(attack)
    oattack = random.choice(attack)
    print "*** " + player + " attacks with: " + pattack.upper()
    print "*** " + opponent + " attacks with: " + oattack.upper()
        

    if pattack == oattack:
        print "It's a tie"
    elif pattack == "dodge" and oattack == "parry":
        ps += 1 
    elif pattack == "parry" and oattack == "dodge":
        os += 1
    elif pattack == "parry" and oattack == "thrust":
        ps += 1 
    elif pattack == "thrust" and oattack == "parry":
        os += 1
    elif pattack == "thrust" and oattack == "dodge":
        ps += 1 
    elif pattack == "dodge" and oattack == "thrust":
        os += 1

    print "Scoreboard: " + player + ": " + str(ps) + " and " + opponent + ": " + str(os)

if ps > os:
    print "The Winner is: " + player
else:
    print "The Winner is: " + opponent