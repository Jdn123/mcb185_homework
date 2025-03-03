"""
import math

def tm(seq):
    a = seq.count('A')
    c = seq.count('C')
    g = seq.count('G')
    t = seq.count('T')

    return (a+t)*2 + (g+c)*4


oligos = ('ATTGCC', 'ATGCCC', 'GCCCCCCCCCC', 'A', 'C')

for oligo in oligos:
    t = tm(oligo)
    print(oligo, t)


import random

things = ['socks', 'pants', 'shirt', 'hat', 'gloves'] # add stuff to list, but not tuple ()

things.append('scarf')

# print(things)

# index
# print(things[0])

for thing in things:
    print(thing)

print(things[0:3])
print(things[0:3:1])
print(things[0:4:2]) #0 -1- 2 -3- 
print(things[0:4:-1]) #empty
print(things[4:0:-1]) #backwards except for [0]
print(things[:3]) #default is start at 0
print(things[0][1]) #gives char 1 of item 0 in list

things = ('socks', 'pants', 'hats', 'socks')

for i in range(len(things)):
    for j in range(i+1, len(things)):
        print(things[i], things[j])



import random

trials = 1000
shared = 0
students = 50
for t in range(trials):
    peeps = [] #list of bday
    for i in range(students): #number of people in class
        bday = random.randint(0,364)
        #peeps.append(bday)
        if bday in peeps:   peeps.append(bday); shared += 1; break #BETTER METHOD
        else:               peeps.append(bday)
    # print(peeps)
    #collision = False
    #for i in range(len(peeps)):
    #    for j in range(i+1, len(peeps)):
    #        if peeps[i] == peeps[j]: collision = True
    #if collision == True: shared += 1


print("prob of shared bday per classroom", shared/trials)    

"""
import random


days = 365
students = 23
trials = 1
shared = 0


for t in range(trials):
    calendar = []
    for i in range(days):
        calendar.append(0)

    print(calendar)

    collision = False
    for i in range(students):
        bday = random.randint(0,364)
        if calendar[bday] == 1:    collision = True; calendar[bday] += 1; break
        else:                       calendar[bday] += 1
    if collision == True:           shared += 1
    print(calendar)

print(shared/trials)