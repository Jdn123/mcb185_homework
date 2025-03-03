import random

# print(savingthrow(5,2))


    #disadvantage(1 throw)   #advantage(2 throw)
#5                 
#10                 
#15                 
"""
for i in range(5,15,5):
    # random.randint(1,20)
    # print(dis, adv)
    dis = (20-i)/20
    adv = throws(2) #total


def throws(): #save is an integer representing the lowest roll for save, repeat is number of throws
    save = 0
    for i in range(2):
        roll1 = random.randint(1,20)
        if save < roll1: save = roll1
    return save
""" 

trials = 1000000
diff = 5
sides = 20

for diff in range(5,16,5):
    nor = 0
    adv = 0
    dis = 0
    for i in range(trials):
        # print(i)
        r1 = random.randint(1,sides)
        r2 = random.randint(1,sides)
        if r1 >= diff: nor += 1
        if r1 >= diff and r2 >= diff: dis +=1
        if r1 >= diff or r2 >= diff: adv +=1
     
    print(diff,  nor/trials, adv/trials, dis/trials)



