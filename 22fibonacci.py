x0 = 0
x1 = 0

for i in range(10):       
    if i < 2: # first two values only: makes sure first two values are 0 and 1 respectively
        x1 = i #i is now
        print("term", i, x0 + x1)
    else:
        total = x0 + x1 # combines previous two terms
        print("term", i, total)
        x0 = x1 # shifts x1 backwards to x0
        x1 = total # initalizes x1 as current term, need total because modify x0 above


y0 = 0
y1 = 1

for i in range(10):       
    if i < 2: # first two values only: makes sure first two values are 0 and 1 respectively
        y1 = i #i is now
        print("term", i, y1)
    else:
        total = y0 + y1 # combines previous two terms
        print("term", i, total)
        y0 = y1 # shifts y1 backwards to y0
        y1 = total # initalizes y1 as current term



# Fn = F(n-1) + F(n-2)
