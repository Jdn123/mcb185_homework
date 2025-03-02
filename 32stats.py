import sys
import math


    
def minmax(vals):
    lo = 0
    hi = 0
    for val in vals:
        if val > hi:    hi = val
        if val < lo:    lo = val
    return lo, hi

def mean(vals):
    tot = 0
    for val in vals:
        tot += val
    return tot / len(vals)

def stdev(vals):
    tot = 0
    avg = mean(vals)
    for val in vals:
        tot += (val - avg) ** 2
    return math.sqrt(tot / (len(vals) - 1))

vals = []
for arg in sys.argv[1:]:
    vals.append(  float(arg)   )

def median(vals):
    strval = '-'.join(sys.argv[1:])
    counts = []

    for arg in sys.argv[1:]:
        x = strval.count(arg)
        counts.append(x)
    #print(counts)


    hi = counts[0]
    #print(hi)
    idx = 0
    for count in counts:
        if count > hi:  hi = count; idx = counts.index(count)

    if vals[idx] == 1:       return None
    else:                    return vals[idx]
        



lo, hi = minmax(vals)

print(vals)
print('# of values: ', len(vals))
print('min is ', lo, ' and max is ', hi)
print('mean is ', mean(vals))
print('standard deviation is ', f'{stdev(vals):.4f}')
print('median is ', median())







