# Build In Functions / Methods

# print function

print ("This is the argument we pass into the print function")

# string function "STR

mytext = "this is a dummy text"
print ("This is the TYPE function: " + str(type(mytext)))
print ("This is the LEN function: " + str(len(mytext)))


print ("This is this upper function: " + mytext.upper())
print ("This is the lower function: " + mytext.lower())
print ("This is the capitalize function: " + mytext.capitalize())
print ("This is the title function: " + mytext.title())

numbers = [4,122,6,3]
print ("This is my numbers array: " + str(numbers))
print ("This is the SUM function: " + str(sum(numbers)))
print ("This is the SORTED function: " + str(sorted(numbers)))

# You can SORT Lists and Dictionaries, but not tuples as they're immutable
names = ["Adam", "Luis", "John"]
print ("This is my list of Names: " + str(names))
print ("This is my SORTED list of Names" + str(sorted(names)))

messy = "         I don't like    to keep   things     even."
print "Prints messy string: " + messy
print messy.strip()







