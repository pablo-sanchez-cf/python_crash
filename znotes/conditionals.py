""" Takes a condition and if it exist, do a set of instructions, 
otherwise it will execute a different set of instructions"""


# CONDITIONAL STATEMENTS 
# IF / ELIF / ELSE

age = int(raw_input("Enter age: "))

if age >= 25:
    result = "Eligible to Rent a car"
elif age >= 21:
    result = "Cant rent a car but can vote"
elif age >= 18:
    result = "Eligible to Vote but not to rent a car"
else:
    result = "Too young to do anything"
print result




