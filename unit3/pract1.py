print('xy'.join(list('ABCDE'))[4:8])

#first it joins A-xy-B-xy-C-xy-D-xy-E into AxyBxyCxyDxyE (0A-1x-2y-3B-4x-5y-6C-7x-8y-9D-10x-11y-12E)
#take indexes 4-7 xyCx

import math

def is_prob(vals):
    tot = 0
    
    for val in vals:
        tot += float(val)
        if val > 1 or val < 0:             return False

    if math.isclose(tot, 1):    return True
    return False

list1 = [0.1, 0.2, 0.3, 0.4]
list2 = [1,2,3]
list3 = [0.1, 0.2, 0.3, 0.4, .9]

print(is_prob(list1))
print(is_prob(list2))
print(is_prob(list3))


vals = [1,2,3,4,5]
vals2 = [1,2,3,4,5,6,7,8,9,10]


def median(vals):
    length = len(vals)
    middle = int(length/2)
    if length % 2 == 1: return vals[math.floor(middle)]
    if length % 2 == 0: return ( vals[middle-1] + vals[middle] ) / 2


print(median(vals))
print(median(vals2))


#length
#print(len(vals))

#middle
#print(len(vals)/2)