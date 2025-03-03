import random
import math


"""
countin = 0
countout = 0

while True:
    dist = math.sqrt((random.random() ** 2) + (random.random() ** 2)) 
    
    if dist <= 1: countin += 1
    if dist > 1: countout += 1
    print( 4 * (countin / (countin + countout)) )

    
    
countin = 0
counttotal = 0

while True:
    dist = math.sqrt((random.random() ** 2) + (random.random() ** 2)) 
    if dist <= 1: countin += 1
    counttotal += 1
    print( 4 * (countin / (counttotal)) )

countin = counttotal = 0


while True: 
    if (math.sqrt((random.random() ** 2) + (random.random() ** 2))) <= 1: countin += 1
    counttotal += 1
    print( 4 * (countin / (counttotal)) )


import random

def max2():
    roll1 = random.randint(1,6)
    roll2 = random.randint(1,6)
    if roll1 > roll2: return roll1
    return roll2

throws = tot = 0
for i in range(10):
    throws += 1
    r1 = max2()
    r2 = max2()
    r3 = max2()
    tot += r1 + r2 + r3
print(tot / throws)


import random

random.seed(12) # get a random seed 12



def load_die(): # more 6 than anything
    r = random.random()
    if r < .1: return 1
    if r < .2: return 2
    if r < .3: return 3
    if r < .4: return 4
    if r < .5: return 5
    return 6

for i in range(100):
    print(random.gauss(0,1)) #random gauss



for i in range(1000):
    count += 1
    # print(count)
    print( 4 / ( (count+1) * (count+2) * (count+3) ))    
    if count%2 == 1: print("+")
    if count%2 == 0: print("-")



count = 0
while True:
    count += 1
    # print(count)
    print( 4 / ( (count+1) * (count+2) * (count+3) ))    
    if count%2 == 1: print("+")
    if count%2 == 0: print("-")

"""

#in class exam: practice

def prime(x):
    if x == 1: return False
    for i in range(2,x):
        if x%i == 0: return False; break
    return True

print(prime(51), prime(47))

for y in range(51, 0, -2):
    if prime(y) == True: print(y, "*", sep='')
    else: print(y)



def prime(x):
    if x == 1: return False
    for i in range(2,x//2 + 1):
        if x%i == 0: return False
    return True

def is_prime(n):
    for den in range(2, n//2 +1):
        if n % den == 0: return False
    return True

print(is_prime(1), prime(1))

