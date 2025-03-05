import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

same = 0

for i in range(trials):
    birthdays = []

    for j in range(people):
        birthdays.append(   random.randint(0, days - 1)    )

    # print(birthdays)
    
    stop = False
    for x in range(people):
        for y in range(x+1, people):
            if birthdays[x] == birthdays[y]:        same += 1;      stop = True;     break
        if stop:                    break
    print( same )

print(same/trials)
    