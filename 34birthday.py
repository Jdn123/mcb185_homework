import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])



# print(len(cal))


same = 0
"""
for i in range( trials ):
    cal = [] #NEED TO SET CAL TO ZERO EVERYTIME

    for i in range(days):
        cal.append( 0 )
    
    births = []

    for j in range(people):
        births.append(   random.randint(0, days - 1)    )

    # print(births)

    for birth in births:
        cal[birth] +=1
    
    # print(cal)

    collision = False

    for c in cal:
        if c > 1:   collision = True

    if collision == True: same += 1
    print(same)
    

print(same/trials)

"""


same = 0

for i in range( trials ):
    iden = []
    cal = [] #NEED TO SET CAL TO ZERO EVERYTIME

    for i in range(days):
        cal.append( 0 )

    collision = False
    for j in range(people):
        birth = random.randint(0, days - 1)
        if cal[birth] > 0: 
            cal[birth] += 1
            #iden.append( birth )
            collision = True
        else: 
            cal[birth] += 1

    # print(cal)

    if collision == True: same += 1
    print(same)
    

print(same/trials)

if '2' in cal: print(True)
else: print(False)

#iden.sort()
#print(iden)


print(cal)


