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

"""
def is_integer(n):
    if n % 1 == 0: return True
    return False

def is_prime(n):
    if n == 0: return False
    for i in range(2, (n/2)):
        if n % i == 0: return False
    return True       

print(is_prime(0))

