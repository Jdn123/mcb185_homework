import random
import sys

entries = int(sys.argv[1]) + 1


tot = 0
for i in range(1, entries):

    end = tot + 1000
    defline ='>'
    linelist = []
    defline = defline + 'Chr' + str(i) + ' ' + str(tot+1) + '-' + str(end)
    tot += 1000
    print(defline)

    lng = random.randint(100, 1000)
    strt = random.randint(1,5)


    for i in range(strt):
        roll = random.randint(1,4)

        if roll == 1:   print('A', end='')
        if roll == 2:   print('G', end='')
        if roll == 3:   print('C', end='')
        if roll == 4:   print('T', end='')
    
    print('ATG', end='')

    for i in range(lng - strt - 3 + 1):
        roll = random.randint(1,4)

        if roll == 1:   print('A', end='')
        if roll == 2:   print('G', end='')
        if roll == 3:   print('C', end='')
        if roll == 4:   print('T', end='')
    
    print('\n')
        


# python3 2pract.py _int_ > dummy.fa




