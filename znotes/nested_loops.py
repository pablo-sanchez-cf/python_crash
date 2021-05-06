# any inner loop needs to finish before the outter loop can terminate




for outter in xrange(1,5):
    for inner in xrange(1,6,2):
        print "Outter Loop: ", str(outter) + " Inner Loop: ", str(inner)