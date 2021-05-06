# Pablo Sanchez
# Python version 2.7.16
# FOR Loops

# Import the Random Module
import random

# Code Name Lists
alpha = ['Crimson', 'Phantom', 'Zephyr', 'Palisade', 'Skyfall', 'Hidden', 'Drastic', 'Golden']
omega = ['Whirlwind', 'Gatecrasher', 'Iceberg', 'Zealot', 'Element', 'Gatekeeper', 'Master', 'Pathfinder']

# CREATE FOR LOOP HERE
# HINT: The line below needs to loop 5 times. In order to receive credit, 
# you must use a FOR Loop. It is a good idea to test the line below to 
# make sure the code name is being generated properly before tackling the
# FOR Loop.

codes = int(raw_input("Enter number of code names to be generated: "))
for names in range(codes):
    print "Operation: " + random.choice(alpha) + " " + random.choice(omega)