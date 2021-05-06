# Pablo Sanchez
# Python version 2.7.16
# FOR Loops

zoo = ['Lion', 'Zebra', 'Giraffe', 'Hippo']

for animal in zoo:
#   if animal == "Lion':  # Closing quotes didn't match.
    if animal == "Lion":
        print "Alex the " + animal
    elif animal == 'Zebra':
#       print "Marty the " + Animal  # Animal is not defined. Needs to be all lower case.
        print "Marty the " + animal
    elif animal == 'Giraffe':
#       print "Melman the " + animals  # animals is not defined. Needs to be singular
        print "Melman the " + animal
    elif animal == 'Hippo':
        print "Gloria the " + animal