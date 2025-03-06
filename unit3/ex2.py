import random
"""
# linex = []
# liney = []

# def dist(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2 ) ** .5

# for i in range(100):
    x = i * .01
    y = x ** 2
    linex.append(x)
    liney.append(y)

# print(linex, liney)

above = 0
below = 0

while True:
    x1 = random.random()
    y1 = random.random()
    

    print('above:', above, 'below:', below, '\n')
    
"""

above = 1
below = 1

while True:
    x1 = random.random()
    y1 = random.random() 

    if y1 > (x1 ** 2):  above += 1
    elif y1 < (x1 ** 2):  below += 1
    else:               None

    # print(above, ':', below, sep='')
    print(above/below)













