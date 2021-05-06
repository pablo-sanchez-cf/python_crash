# Pablo Sanchez
# Python version 2.7.16
# Error/Exception Handling
#
#
###################################################################################################
import random
import time

# Custom Functions
# 2. ADD THE agecheck() CUSTOM FUNCTION YOU CREATED HERE
def agecheck(a):
    print ("Confirming you're " + str(age) + " years old")

age = int(raw_input("Enter age: "))
agecheck(age)

##################################################################################################
# 3. DESCRIBE HOW THE INCLUDED countdown() FUNCTION WORKS
# A: Looks at the value of "n" and it will keep substracting 1 as long as the value is more or equal to zero.
#    Also it uses the time module with 1 second delay while printing the outout of the substraction
def countdown(n):
    while n >= 0:
        print n
        time.sleep(1)
        n -= 1

##################################################################################################
# Self Destruct Sequencer
# This is the custom function created to handle all of the Self Destruct
# features needed. There are a few steps involved in the process, so take a few
# moments to study how this function works and think about ways to make it better.
def self_destruct(x):

    # Set Destruct Codes
    authorized_test = "000-Destruct-0"
    authorized_final = "000-Destruct-1"

    # 4. CREATE VARIABLES (SIMILAR TO ABOVE) FOR THE COMMANDING OFFICER'S CODE (co_code)
    # EXECUTIVE OFFICER'S CODE (xo_code) & CHIEF ENGINEER'S CODE (ce_code)
    co_code = "111A-Destruct"
    xo_code = "21A2B-Destruct"
    ce_code = "31B2B-Destruct"

##################################################################################################
    # Consider the following print statements. Could they be combined into a single print
    # statement and get the same result? (Answer: Yes) There are many ways to resolve
    # issues in scripting. You get to decide what works best for your script.
    #  Display Self Destruct Warning
    print "--------------------- WARNING! ----------------------"
    print "You have initiated the USR ARES Self Destruct Program"
    print "_____________________________________________________"
    print "You must provide Authorized Initiate Code to Proceed."

##################################################################################################
    # Request Authorized Rank
    # 5. EXPLAIN THE SIGNIFICANCE OF THE int() FUNCTION IN THE FOLLOWING LINE:
    rank = int(raw_input("Select Correct Rank:\n [1] Commanding Officer\n [2] Executive Officer\n [3] Chief Engineer\n RANK: "))
    # A. To enfoce that the value entered by the user and stored as "rank" is treated as an integer and not as a string.

##################################################################################################
    # Because we're expecting the user to enter a number above, the conditional statement
    # below is needed to convert those numbers into something more useful. Doing this helps
    # reduce the risk of the user introducing bad data into the script.
##################################################################################################
    # Retrieve Rank Initiate Code
##################################################################################################
    # Commanding Officer
    if rank == 1:
        code = co_code
        print "Commanding Officer Confirmed."
    # Executive Officer
    elif rank == 2:
        code = xo_code
        print "Executive Officer Confirmed."
    # Chief Engineer
    elif rank == 3:
        code = ce_code
        print "Chief Engineer Confirmed."
    else:
        print "You are not authorized to initial Self Destruct."


##################################################################################################
    # Enter Self Destruct Code: 000-Destruct-0 or 000-Destruct-1
##################################################################################################
    # Set Supplied Rank Code
    initiate = raw_input("Enter Self Destruct Confirmation Code: ")

    # Compare Rank Codes
    while initiate == code:
        print "Self Destruct Initiate Code: ACCEPTED"
        final_code = raw_input("Enter Activation Code: ")
        if final_code == authorized_final:
            print "Destruct Sequence Confirmed."
            # 6. EXPLAIN THE SIGNIFICANCE OF THE str() FUNCTION HERE
            print str(x) + " seconds to Self Destruct."
            # A. converts the value of x into a string so that it can be concatenateed with the rest of the print message.
            print "ALL HANDS ABANDON SHIP - THIS IS NOT A DRILL"
            countdown(x)
            print "Have a nice day!"
            print "BOOM!"
        elif final_code == authorized_test:
            print "Destruct Sequence Test Order Confirmed."
            print "THIS IS A DRILL - THIS IS A DRILL"
            print "Timer Set to: " + str(x) + " seconds."
        else:
            print "Destruct Sequence Aborted."


##################################################################################################
    # Program Ends
##################################################################################################
# Self Destruct
timer = int(raw_input("Enter Countdown Length (in seconds): "))
self_destruct(timer)



# 6. LIST THE LOCAL VARIABLES AND GLOBAL VARIABLES USED THROUGHOUT THIS SCRIPT
# A. "age" line 15 (global variable)
# A. "n" line 24
# A. "authorized_test" line 37
# A. "authorized_final" line 38  
# A. "co_code" line 42
# A. "xo_code" line 43
# A. "ce_code" line 44
# A. "rank" line 59
# A. "code" lines 71, 75, 79
# A. "initiate" line 89
# A. "final_code" line 94
# A. "timer" global variable in line 116

# 7. LIST THE BUILT IN FUNCTIONS USED THROUGHOUT THIS SCRIPT
# A. raw_input
# A. print
# A. str
# A. int
# A. time.sleep

# 8. LIST THE MODULE FUNCTIONS USED THROUGHOUT THIS SCRIPT
# A. random
# A. time

# 9. LIST THE CUSTOM FUNCTIONS USED THROUGHOUT THIS SCRIPT
# A. agecheck()
# A. countdown()
# A. self_destruct()
