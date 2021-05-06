# Custom Reusable blocks of code (FUNCTIONS)

'''
1 - Whatever name we decide to use to name a function, cannot be a reserved keyword or an existing python built-in function or external modules.
2 - You must first define a function before it can be used.
3 - Some functions can be created without a required argument to be passed () 
'''

# Define the custom function
def printmessage(x):    
    print "This is what you just typed: " + x             

# Assigning text to a variable
mymessage = raw_input("Enter message: ")

# calling the function into action and passing it the variable
printmessage(mymessage)