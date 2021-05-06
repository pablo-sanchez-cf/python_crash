# Pablo Sanchez
# Python version 2.7.16
# Pirate Swashbuckle Fight Milestone 3

# 1. Import the utilities file
import utilities

# 2. Import the pirates.txt file
pirates = utilities.filereader('pirates.txt')

# dodge > parry > thrust > dodge
attack =['dodge', 'parry', 'thrust']

# 3. Use the utilites to randomly pick pirates for player and opponent
player = utilities.randompicker(pirates)
opponent = utilities.randompicker(pirates)

# 4. Add a while loop so that the pirates are not the same

while player == opponent:
    opponent = utilities.randompicker(pirates)

print "Advast ye swabs, a fight betwixt \n" + player + " & " + opponent + " 'tis bout to commence! "

pscore = 0
oscore = 0
gameover = False

while gameover == False:
    # This has changed for milestone 3. The game will still end when the player or opponent reaches 3. 
    if pscore >= 3:
        print "_" * 50 + "\n"
        print player + " has vanquished " + opponent
        print "Hip hip huzzah!"
        gameover = True
        break
    elif oscore >= 3:
        print "_" * 50 + "\n"
        print opponent + " has vaquished " + player
        print "Oh Captain, my Captain!"
        gameover = True
        break
    # 5. Exception - Add a while True and exception. 
    # Example: the player attack variable should allow the user to pick between the different types     

    while True:
        try:
            pattack = int(raw_input("Player, please pick your Attack:\n[1] dodge\n[2] parry\n[3] thurst\n>> "))
            if pattack > 0 and pattack < 4:
                break
            else:
                print "Invalid Selection, Try Again\n >>" 
        except ValueError:
            print "Invalid Selection, Try Again\n >>"

   # 6. Player only - Create an if/elif statement to set the number entry to the correct attack.

    if pattack == 1:
        pattack = "dodge"
    elif pattack == 2:
        pattack = "parry"
    elif pattack == 3:
        pattack = "thrust"
    else:
        print ("Invalid Option, Select an Option from 1 to 3")


    # The program randomly picks the attack for the opponent

    oattack = utilities.randompicker(attack)

    # 7. Add a while loop so that the attacks are not the same. Use the utilities module.
    
    while pattack == oattack:
        oattack = utilities.randompicker(attack)

    print player + " attacks with a " + pattack
    print opponent + " attacks with a " + oattack

    # 8. Change your if/elif statment. Use the and to compare the attacks. All attacks must be used correctly.
   
    if pattack == "dodge" and oattack == "parry":
        print (player + " defeats " + opponent)
        pscore += 1
    elif pattack == "parry" and oattack == "thrust":
        print (player + " defeats " + opponent)
        pscore += 1
    elif pattack == "thrust" and oattack == "dodge":
        print (player + " defeats " + opponent)
        pscore += 1
    elif oattack == "dodge" and pattack == "parry":
        print (opponent + " defeats " + player)
        oscore += 1
    elif oattack == "parry" and pattack == "thrust":
        print (opponent + " defeats " + player)
        oscore += 1
    elif oattack == "thrust" and pattack == "dodge":
        print (opponent + " defeats " + player)
        oscore += 1
   
    # 9. Print a string that includes the player and the players score.
    print (player + ": " + str(pscore) + " points")
   
    # 10. Print a string that includes the opponent and the opponents score.
    print (opponent + ": " + str(oscore) + " points\n")