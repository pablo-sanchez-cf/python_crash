# Pablo Sanchez
# Python version 2.7.10
# Congress Age Checker

# raw_input() allows the user to enter a value for the variable 'age'
# str() tells python to treat the value as a string
# "Enter Age: " is the prompt that will appear to the user when the script is executed
age = int(raw_input("Enter Age: "))

# Using the above as a guide, complete the following line so that
# "Enter Number of years as a US Citizen: " will appear when the script is executed
citizen = int(raw_input("Enter citizenship length in years: "))

# Conditional Statement
# Using the variables 'age' & 'citizen', construct a conditional statement that will
# check to see is the user is eligible for the Senate, House of Representatives, both or neither.
# To help you get started the first condition has been provided for you

if age >= 30 and citizen >= 9:
    print "You are eligible for the Senate and the House "
elif age >= 25 and citizen >= 7:
    print "You are eligible for the House of Representatives."
else:
    print "You are ineligible to serve."