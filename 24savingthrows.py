import random


def savingthrow(save, repeat): #save is an integer representing the lowest roll for save, repeat is number of throws
    tot = 0
    for i in range(repeat):
        tot += random.randint(1,20)
    return (tot/repeat > save)



print(savingthrow(5,2))

