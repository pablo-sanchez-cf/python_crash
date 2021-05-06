# LOOPS

# 1) FOR loops

for x in range(0, 20):
    print x

for x in xrange(10):
    if x == 5:
        print "You've landed at 5"
        continue
    print (x)

for x in xrange(10):
    if x == 5:
        print "You've landed at 5"
        break
    print (x)


for x in xrange(1, 22):  # the numbers in xrange mean, start, stop and step.
    print x
    if x >= 17 and x < 21:
        print "close but not cigar"
        continue
    elif x == 21:
        print "Blackjack"

# setting a list to loop

colors = ['red', 'white', 'blue']
for color in colors:
    print colors

# 2) WHILE Loop

while True:
    n = raw_input("enter 'hi': ")
    if n.strip() == "hi":
        print "Hello!" 
        break