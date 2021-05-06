'''
Variables are local when they are only defined within a custom function
In the below example, X is a local variable. It only exists inside the function and cannot 
be called from somewhere else in the script '''

def printmessage(x):
    print x

x = "I am a meat popsicle"
# Define Function
def squarethis(x):
    return x * x

mynumber = squarethis(3)
print x
print mynumber

# In the above example "X" only lives inside the custom function "squarethis" 

# Below Global vs Local variable shows how variable in local cannot be referenced from outside the function

T = "This is a Global T"
def useaglobal():
    global T
    print ("Printing from Global Function: " + T)

def localonly(x):
    T = "This is local T"
    print ("Printing from Local Function: " + T)

useaglobal()
localonly(T)