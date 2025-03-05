import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

cal = []

for i in range(days):
    cal.append( 0 )

# print(len(cal))


same = 0

for i in range( trials ):
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

    if collision: same += 1
    

print(same/trials)







