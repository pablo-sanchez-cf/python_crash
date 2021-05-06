# Random Module will not work on tuples as they're immutable
import random

numbers = [4, 5 ,7, 9, 2, 1]
print ("print list as it is: " + str(numbers))
random.shuffle(numbers)
print ("print list after applying SHUFFLE: " + str(numbers))
random.choice(numbers)
print ("print list after applying RANDOM OVER SHUFFLE: " + str(numbers))