# Pablo Sanchez
# Python version 2.7.16
# Importing & Exporting Data

# Input / Output

# w write permissions
# w+ write permissions w\create blank doc
# r read only permission
# a append

#######################
# MLB TEAMS
#######################

# 2. The example below uses the old method of opening an external file.
# Convert the open() function below [line 16 - 18 ]to with open().

# Baseball Team Text file import
'''
CONVERTING TO WITH OPEN()
f = open('mlb-teams.txt', 'r')
mlb = f.read().splitlines()
f.close()


WITH OPEN METHOD
with open ('mlb-teams.txt', 'r') as f:
'''


# 3. Replace the w+ with the appropriate option for appending the file.
with open('mlb-teams.txt', 'a') as f:

    # 4.  Using the f.write() function, add three more teams to the list:
    # [ Seattle Pilots, Washington Senators & Montreal Expos ]
    f.write("Seattle Pilots\n")
    f.write("Washington Senators\n")
    f.write("Montreal Expos\n")


#######################
# HALL OF FAME PLAYERS
#######################

favorite_baseball_player = "Old Hoss Radbourne"

with open("hall_of_fame.txt", 'w+') as f:
    f.write("Bobby Bonds\n")
    f.write("Al Kaline\n")
    f.write("Mickey Mantle\n")
    f.write("Willie Mays\n")

    # 5. Using the f.write() function, add the player stored in
    # favorite_baseball_player to the hall_of_fame.txt file
    # Note: You MUST reference the variable in this part.

    f.write(favorite_baseball_player + '\n')
    f.write('\n')

# 6. Replace the r with the appropriate option for appending the file.
with open("hall_of_fame.txt", "a") as f:

    # 7. Using the f.write() function, add 3 more players the list:
    # [Babe Ruth, Willie Stargell & Roberto Clemente]
    f.write("Babe Ruth\n")
    f.write("Willia Stargell\n")
    f.write("Roberto Clemente\n")

# 8. Using with open(), place the values stored in hall_of_fame.txt into a variable called hof_players
with open ("hall_of_fame.txt", "r") as f:
    hof_players = f.read().splitlines()

# 9. Write a print statement below with the MLB Team closest to your Home Town.
with open("mlb-teams.txt", "r") as f:
    teams = f.read().splitlines()
    print ("MLB Team closest to my Home Town: " + teams[17])

# 10. Write a print statement to print one of the players stored in the variable hof_players created in step 8.
print ("Player from HoF: " + hof_players[3])