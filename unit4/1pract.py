import sys
import mcb185
import math


lngs = [] #store lengths
idxs = 0    #indexing
#counts would be idxs+1 because idxs start at 0
low = 10000 #max
hi = 0      #min
avg = 0
stdev = 0


for defline, seq in mcb185.read_fasta(sys.argv[1]):
    

    lngs.append(len(seq))
    idxs += 1

    if len(seq) < low: 
        low = len(seq)

    if len(seq) > hi:
        hi = len(seq)

tot = 0
for lng in lngs:
    tot += int(lng)
avg = tot / len(lngs)

tot1 = 0
for lng in lngs:
    tot1 += (int(lng) - avg) ** 2
stdev = math.sqrt(tot1/ (len(lngs)-1))

lngs.sort(reverse=True)
collision = 0
hold_idx = 0
tot2 = 0
#use tot from above should still be sum of all lengths
for i, lng in enumerate(lngs):
    #print(lng)
    tot2 += lng
    if tot2 < (tot/2):
        hold_idx = i
    else:
        collision += 1
        if collision > 1: 
                break
        hold_idx = i
#n50 is lngs[hold_idx]
    

print(lngs, idxs + 1, low, hi, avg, stdev, lngs[hold_idx], sep='\n')






