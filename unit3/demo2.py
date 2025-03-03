import sys
import math

list = []
for arg in sys.argv[1:]:
    f = float(arg)
    list.append(f)
    # print(arg)

##############################################################################

def n50(list):
    list.sort()
    tot = 0
    for item in list:
        tot += item
    halfway = 0
    index = 0
    while (halfway < (tot / 2)):
        index += 1
        halfway = list[index]
    return list[index]

###############################################################################

def mean(list):
    tot = 0
    for num in list:
        tot += num
    return tot / len(list)

def stdev(list):
    variance = 0
    for num in list:
       variance += (num - mean(list)) ** 2
    return math.sqrt(variance/len(list))

def zscore(list, index):
    zmean = mean(list)
    zstdev = stdev(list)

    return (list[index] - zmean) / zstdev

def zrange(list, range):
    upper = mean(list) + range * stdev(list)
    lower = mean(list) - range * stdev(list)
    return upper, lower

def zall(list):
    scores = []
    zmean = mean(list)
    zstdev = stdev(list)
    for i in range(len(list)):
        scores.append( (list[i] - zmean) / zstdev  )
    return scores

# or
 
def zall1(list):
    scores = []
    for i in range(len(list)):
        scores.append(zscore(list, i))
    return scores
        

print(zscore(list, 5))
u, d = zrange(list, 1) 
print('upper:', u, ' lower:', d, sep = '')   
print(zall(list))
print(zall1(list))

        


