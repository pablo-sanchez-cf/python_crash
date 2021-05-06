import random

def randompicker(P):
    random.shuffle(P)
    return random.choice(P)

def filereader(T):
    with open(T,'r') as f:
        return f.read().splitlines()