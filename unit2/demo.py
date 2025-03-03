"""

def triangular(n):
    total = 0
    for i in range(1, n+1):
        total = total + i
    return total

# print(triangular(4))

def fact(n):
    total = 1
    for i in range(1, n+1):
        total = total * i
    return total

# print(fact(2))

import random

i = 0
while i<5:
    i = i + 1
    #print(random.random())
    pass

for i in range(10):
    #print(random.randint(1,6))
    pass

total_total = 0

rep = 1000



# example one: rep
total = 0
for i in range(rep):
    throws=0
    for j in range(3):
        r = random.randint(1,6)
        throws += r
    # print(total1)
    total += throws

# print(total/rep)

import math

def factorial(n):
    if n==0: return 1
    product = 1
    for i in range(1, n+1):
        product *= i
    return product

# e = 1 + 1/n!

e = 0
for n in range(20):
    e += 1 / factorial(n)
    print(e)

def is_integer(n):
    if n % 1 == 0: return True
    return False

def is_prime(n):
    if n == 0: return False
    for i in range(2, (n/2)):
        if n % i == 0: return False
    return True       

print(is_prime(0))

# monty python

import random
import math

def twopoint(x1,y1,x2,y2):
    xdist = abs(x1-x2)
    ydist = abs(y1-y2)
    combine = pow(xdist,2) + pow(ydist,2)
    return math.sqrt(combine)


countin = 0
countout = 0
# print(countin, countout)



for i in range(1000000):
    x = random.random()
    y = random.random()
    distance = twopoint(x,y,0,0)
    print(x, y, distance)
    if distance <= 1.0:
        # print("in circle")
        countin += 1
    if distance > 1.0:
        # print("out circle")
        countout += 1

# print(countin, countout)

total = countin + countout
pi = 4 * (countin / total)
print(pi)


#PRACT EXAM 1

pi4 = 0
i = 1
odd = 2

while True:
    if odd%2 == 0: pi4 += 1 / i
    else: pi4 -= 1 / i
    print(pi4 * 4)
    i += 2
    odd += 1



#PRACT EXAM 2
import random


trial = 20
revive = 0
death = 0
roll = 5


for attemps in range(trial):
    save = 0
    fail = 0
    print("attempt", attemps)
    for r in range(roll):
        max_roll = 0
        r1 = random.randint(1,20)
        r2 = random.randint(1,20)

        print(r1, r2)

        if r1 > r2: max_roll = r1
        else: max_roll = r2

        if max_roll == 1:                           fail += 2
        elif max_roll > 1 and max_roll < 10:        fail += 1
        elif max_roll >= 10 and max_roll < 20:      save += 1
        else:                                       revive += 1; break
    if save == 3: revive += 1
    if fail == 3: death += 1
        
          

print("trials", trial, "revive rate", revive/trial, "death rate", death/trial)

#PRACT EXAM 3

pi4 = 0
i = 1
odd = 2

while True: #replace this with a statement like i < 200000 or use a for loop: for t in range(200000)
    if odd%2 == 0: pi4 += 1 / i
    else: pi4 -= 1 / i
    print(pi4 * 4)
    i += 2
    odd += 1


print(round(1.1))

if round(1.1) == 1: print(True)

for i in range(1, round(5.1)):
    print(i)

"""
import random

#four rule sets
#rule 1
#rule 2
#rule 3
#rul2 4

def low4(a,b,c,d):
    low = a
    if b < low: low = b
    if c < low: low = c
    if d < low: low = d
    return low

def stats3D6():
    total = 0
    for i in range(3):
        total += random.randint(1,6)
        # print(i)
    return total

def stats3D6r1():
    total = 0
    i = 0
    while i < 3:
        g = random.randint(1,6)
        if g != 1: 
            total += g
            i += 1
        # print(g, i)
    return total

def stats3D6x2():
    total = 0   
    for i in range(3):
        r1 = random.randint(1,6)
        r2 = random.randint(1,6)
        if r1 >= r2:    total += r1
        else:           total += r2
        # print(r1, r2)
    return total

def stats4D6d1():
        r1 = random.randint(1,6)
        r2 = random.randint(1,6)
        r3 = random.randint(1,6)
        r4 = random.randint(1,6)
        # print(r1, r2, r3, r4)
        return r1 + r2 + r3 + r4 - low4(r1, r2, r3, r4)

repeat = 10000

functions = (stats3D6, stats3D6r1, stats3D6x2, stats4D6d1)
for i, func in enumerate(functions): #no need enumerate
    total = 0
    for j in range(repeat):
        total += func()
    # print(func, total/repeat) #func is functions[x]

names = ('3D6', '3D6r1', '3D6x2', '4D6d1')

for name, func in zip(names, functions):
    total = 0
    for j in range(repeat):
        total += func()
    # print(name, ': ' ,total/repeat, sep='')




def nilakantha(limit): 
    g = 3
    for i in range(2, limit, 2):
        j = (i / 2) + 1
        if j%2 == 0: g += 4 / (i * (i+1) * (i+2))
        else: g -= 4 / (i * (i+1) * (i+2))
    return g

# print(nilakantha(10000))

import math

def factorial(n):
    total = 1
    for i in range(n, 0, -1):
        total *= i
        # print(total)
    return total

for i in range(4):
    (factorial(i))

def poissonprob(k, n):
    return (n ** k) * (math.e ** -n) / factorial(k)

# poissonprob(1, 2)

def euler(n):
    total = 0
    for i in range(1, n):
        total += 1/factorial(i)
    return total

#print(euler(2000))

pi4 = 0
i = 1
odd = 2

while round(pi4 * 4, 6) != 3.14159:
    if odd%2 == 0: pi4 += 1 / i
    else: pi4 -= 1 / i
    print(pi4 * 4)
    i += 2
    odd += 1


