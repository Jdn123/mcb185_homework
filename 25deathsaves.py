import random

# = 20 recover
# > 10 success
# 0 < < 10 failure
# 0 2 failure

#3 success = recover
#3 failure = dead

# only 5 throws
import random

trials = 5

die = 0
revive = 0

for i in range(trials):
    print('trial', i)
    win = 0 # number of successes
    fail = 0 # number of failures
    for j in range(5):
        r = random.randint(1, 20) # number of rolls
        # print(r)
        if r == 1:                      fail += 2
        elif r <= 9:                    fail += 1
        elif r <= 19:                   win += 1
        else:                           revive += 1; print('revive'); break
    if win == 3:                        revive += 1; print('revive')
    if fail == 3:                       die += 1;    print('die')

print(die, revive)


"""

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

"""