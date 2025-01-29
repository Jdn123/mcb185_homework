import math

print('A')
def twopoint(x1,y1,x2,y2):
    xdist = abs(x1-x2)
    ydist = abs(y1-y2)
    combine = pow(xdist,2) + pow(ydist,2)
    return math.sqrt(combine)

print(twopoint(1,1,2,2))

print('B')
def harmonicmean(a, b, c, d):
    n = 4
    sm = (1/a) + (1/b) + (1/c) + (1/d)
    return n/sm

print(harmonicmean(5, 6, 7, 8))

print('C')
def max4(a,b,c,d):
    tmmax = a
    if tmmax < b: tmmax = b
    if tmmax < c: tmmax = c
    if tmmax < d: tmmax = d
    return tmmax
print(max4(1,10,55,9))