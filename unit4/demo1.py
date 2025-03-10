
demo = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]

w = 3


for i in range(0, len(demo)-w +1, w): #need that +1 otherwise, the loop terminates too early
    print(demo[i:i+3])

print()

for i in range(0, len(demo)-w, w):
    print(demo[i:i+3])

print()

x = 2

for i in range(0, len(demo)-x+1, x):
    print(demo[i:i+x])

print()

for i in range(0, len(demo)-x, x):
    print(demo[i:i+x])

print()

y = 1


for i in range(0, len(demo)-y+1, y):
    print(demo[i:i+y])

print()

for i in range(0, len(demo)-y, y):
    print(demo[i:i+y])


