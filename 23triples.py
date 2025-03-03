
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

g = 0
while g < 100000: # g < 10000
    a = random.randint(1,100)
    b = random.randint(1,100)
    c = random.randint(1,100)

    if pytha(a, b, c) == True: print(a, b, c)
    g += 1

"""
limit = 100
for a in range(1, limit):
    # print(a)
    for b in range(a+1, limit): #don't check numbers under 1 ie: 3 4 5, 4 3 5 also work so b
                                # should always be greater than a
        c = math.sqrt((a**2 + b**2))
        if c%1 == 0: print(a, b, c)
        


