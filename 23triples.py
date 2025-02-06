
#smallest triple is 3,4,5

import math
import random

def hypo(a, b):
    return math.sqrt((a**2 + b**2))

def pytha(a, b, c):
    if c**2 == (a**2 + b**2): return True
    return False
"""
while True:
    a = random.randint(1,100)
    b = random.randint(1,100)

    if hypo(a, b)%1 == 0: print(a, b, hypo(a,b))
"""
while True:
    a = random.randint(1,100)
    b = random.randint(1,100)
    c = random.randint(1,100)

    if pytha(a, b, c) == True: print(a, b, c)