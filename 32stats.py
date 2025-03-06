import sys
import math

vals = []
for arg in sys.argv[1:]:
    vals.append(  float(arg)   )


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


def mode(vals):
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
        
def n50(vals):
    vals.sort(reverse = True)
    
    tot = 0
    for val in vals:
        tot += val

    # print(tot)

    half = 0
    lng = 0
    i = 0
    while half < (tot/2):
        half += vals[i]
        # print(' half ',half, ' lng ', end='')
        lng = vals[i] # need to set lng before adding i, otherwise the you are getting the next item not the current
        
        #set loop at the end
        i += 1
        #print(lng)

        
    
    return int(lng)

def n50a(vals):
    vals.sort(reverse = True)

    tot = 0
    for val in vals:
        tot += val
    
    halfsum = 0
    lng = 0
    
    #print(tot)
    #print('total/2', tot/2)

    for val in vals:
        halfsum += val
        #print(halfsum)

        if halfsum > (tot/2):  
            lng = val 
            break

        
        # print('n50', lng)
           
    return int(lng)
        

def n50b(list):
    list.sort()
    tot = 0
    for item in list:
        tot += item

    #print(tot)

    halfway = 0
    idx = 0
    while (halfway < (tot / 2)):
        idx += 1
        halfway += list[idx]
    return int(list[idx])










lo, hi = minmax(vals)

#"""
print(vals)
print('# of values: ', len(vals))
print('min is ', lo, ' and max is ', hi)
print('mean is ', mean(vals))
print('standard deviation is ', f'{stdev(vals):.4f}')
print('median is ', mode(vals))

#"""

#print(vals)
print('n50')
print(n50(vals))
print(n50a(vals))
print(n50b(vals))






