import sys
import math

probs = []
for arg in sys.argv[1:]: # convert everything after argv[0] which is the file name into probs
    f = float(arg)
    if f <= 0 or f >= 1: sys.exit('error: not a probability') # make sure probability is real
    probs.append(float(arg)) # add to list

#sys.exit completely terminates program, break just terminates a loop

total = 0
for p in probs: total += p # total up the probs
if not math.isclose(total, 1.0): # tot is not close to 1.0: all probabilities need to add up to 1
    sys.exit('error: probs must sum to 1.0') # return error

h = 0
for p in probs: # calculate entropy
    h -= p * math.log2(p) # negative sum of mat.log2(p)

print(f'{h:.4f}') #4 digits after decimal
