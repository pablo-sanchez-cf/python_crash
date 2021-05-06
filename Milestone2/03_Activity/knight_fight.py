# Pablo Sanchez
# Python 2.7.16
# Tale of the Black Knight

# The random module provides access to random related functions
# The time module provides access to time related functions
import random
import time

goodguy = str(raw_input("Enter your Knight's Name: "))
goodguy = "Sir " + goodguy

# Here, we are assigning the value 'The Black Knight' to the variable badguy
# 1. CHANGE THIS LINE SO THE USER CAN ENTER A VALUE FOR BADGUY
badguy = str(raw_input("Enter the Bad Guy's Name: "))
badguy = "Sir " + badguy

# Once Upon A Time...
print goodguy + ", a Knight in search of adventure, is wandering through the enchanted forest one day."

# 2. WHAT ACTION IS THIS LINE PERFORMING?
# A: This allows the user to read the previous print statement. This will delay the next line execution 2 seconds.
time.sleep(2)

print "As " + goodguy + " reaches a clearing, he encounters the fearsome " + badguy + "!"

time.sleep(2)

print goodguy + ": You, Sir, are a Blackguard and a coward! I challenge you to a duel!"
print badguy + ": I'mma cut you, fool!"

# Good Guy Health
gghealth = 100
# Bad Guy Health
bghealth = 100

# Fight Sequence Loop
while True:
    # 3. EXPLAIN HOW GOODGUY / BADGUY HIT POINTS ARE GENERATED
    # A: They're generated randomly with numbers between 1 to 100 using the Random randint() Method
    # Good Guy / Bad Guy Hit Points
    gghit = random.randint(1, 100)
    bghit = random.randint(1, 100)
    # #######################################################

    # 4. WHAT PURPOSE DOES '\n' SERVE?
    # A: Prints a new line
    print "\n"

    # 5. FIND & CORRECT THE SYNTAX ERRORS. COMMENT OUT THE INCORRECT LINE AND
    # WRITE THE CORRECT CODE UNDERNEATH
    # print goodguy + " rolls a " + gghit
    print goodguy + " rolls a " + str(gghit)
    # print badguy + " rolls a " + bghit
    print badguy + " rolls a " + str(bghit)

    # 6. EXPLAIN HOW THE VALUE IN DAMAGE IS CALCULATED
    # A: Is the difference of substracting the hits of good guy minus the hits of bad guy. If the good guy hits are higher. 
    #    This is decreasing the health value as well.
    # Damage Calculator
    if gghit > bghit:

        damage = gghit - bghit
        bghealth = bghealth - damage
        print goodguy + " strikes " + badguy + " for a " + str(damage) + " hit!\n"

        if bghealth >= 100:
            print badguy + ": Thou hast missed.\n"
        elif bghealth >= 75:
            print badguy + ": Tis but a flesh wound.\n"
        elif bghealth >= 50:
            print badguy + ": Alas! A fair strike! En garde!\n"
        elif bghealth >= 25:
            print badguy + ": Thou art a worthy opponent.\n"
        elif bghealth < 10:
            print badguy + ": I am beaten. Well fought...\n"
            break
    # #######################################################
    elif bghit > gghit:

        damage = bghit - gghit
        gghealth = gghealth - damage

        # 7. EXPLAIN WHY THE str() FUNCTION IS NEEDED HERE
        # A: Because is not possible to concatenate Strings and Integers. str makes the int value of damage become a string.
        print badguy + " strikes " + goodguy + " for a " + str(damage) + " hit!\n"

    # 8. CORRECT THE SYNTAX ERROR(S)
    #   if gghealth = 100:
        if gghealth >= 100:
            print goodguy + ": Thou hast missed.\n"
        elif gghealth >= 75:
            print goodguy + ": Tis but a flesh wound.\n"
        elif gghealth >= 50:
            print goodguy + ': Alas! A fair strike! En garde!\n'
        elif gghealth >= 25:
    #       print goodguy ": Thou art a worthy opponent.\n"
            print goodguy + ": Thou art a worthy opponent.\n"
        elif gghealth < 10:
            print goodguy + ": I am beaten. Well fought...\n"
            break
    # #######################################################

# END OF LOOP ###############################################

# 9. PRINT A CONGRATULATORY STATEMENT HERE USING THE NAME OF THE WINNER (GOODGUY OR BADGUY)


print "End of the Knight Fight\n"

if gghealth > bghealth:
    print "Congratulations " + goodguy + "!"
else:
    print "Congratulations " + badguy + "!"


# PART 2
'''
In your own words, answer the following 4 questions on the use of the WHILE Loop in the script from Part 1:

    1. What Condition will end the WHILE Loop? 
       The WHILE loop will break when the health of on the knights is less than 10. Otherwise it will continue to be True.     
    2. How is that Condition handled in the code?
       It is handled by evaluating the value of gghealth and bghealth using IF/ELIF multiple statements.
    3. What events happen inside the WHILE Loop?
       A Hit for good and bad guys are generated randomly. A damage is calulated. A health score is calculated.
    4. Why are gghealth & bghealth initially set outside the WHILE Loop?
       These variables need to have an initial value to be later used in the loop. Same as bad and good guys names handled by raw_input.
'''

# 10. AFTER completing upload your completed script as a .zip file to FSO
