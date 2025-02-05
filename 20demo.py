## Unit 2 

#Tuples
x = 1, 2
# print(x[0]) #note: tuple strats at 0,1,2...
# print(x[1]) #2

def midpoint(x1, y1, x2, y2):
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    return x, y

mid1 = midpoint(1,2,3,4)
# print(mid1[0], mid1[1]) #return x, y

mx, my = mid1 #this also works, unpacking a tuple, generally better than using indices
# print(mx, my)

#Iteration
"""
#WHILE loop
t = 0
while True: #while followed by a boolean statement, infinite
    # print("repeat", t)
    t += 1

m = 0
while True: #while followed by a boolean statement, infinite
    # print("repeat", m) 
    m += 1
    if m == 1: break #break stops iteration: usually use with boolean expression
    
g = 0
while g < 20: #20 times, then while stops
    # print("repeat", g)
    g += 1

    
#IF loop
k = 0
for i in range(0, 20, 2): #i starts at 0, loops stops when i = 20, add 2 to i every loop
    print("repeat", k)
    k += 1


#for i in range(0, 10) #default increment by 1
#for i in range(10) #default start at 0 and increment by 1


ls = 'milk', 'egg', 'bread', 'bacon', 'celery', 'chicken', 'orange'
for item in ls: #counts "items", and iterates by 1
    print(item)

ls = 'milk', 'egg', 'bread', 'bacon', 'celery', 'chicken', 'orange'
for i in range(len(ls)): #len counts the number of items in ls, default settings for start and increment
    print(ls[i])

"""    

#Nesting
#Using conditionals inside of loops

even = 0
odd = 0

for i in range(7): 
    if i % 2 == 0: even += 1;    # print(i, 'is even')  #; to keep things on the same line
    else:          odd += 1;     # print(i, 'is odd')   

#Random Numbers

import random

# print(random.random()) # produces a number 0 <= # < 1
# random.seed(1) # seed 1
# print(random.randint(1,6)) # dice roll, prints a number between 1 <= 1 <= 6

#Compound Assignment
x = 0
x += 1
#print(x) #1

# -= 1 # subtract 1
# *= 1 # mutliple by 1
x *= 1
#print(x) #1






