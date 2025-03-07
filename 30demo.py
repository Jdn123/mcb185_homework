
grades = 'abcdef'
# for nt in grades:
    # print(nt, end = '') # remove lines



repeat = 'A'
# for i in range(10):
  #  repeat = repeat + 'a'
  #   print(repeat)

alphabet = 'abcdefghijklmnopqrstuvwxyz'

# for i in range(len(alphabet)):
    # print(i+1, alphabet[i])

'hello world' 'hell wrld' 'hell wild'

s = 'hello world'
# print(s.replace('o', '').replace('r', 'i')) # note second replace, changes the previous replace not the og

import math

#dna = 'ATGCTGTAA'
#for i in range(0, len(dna), 3):
 #   codon = dna[i:i+3]
 #   print(i, codon)

"""
print(f'{math.pi}')            # does nothing special
print(f'{math.pi:.3f}')        # 3 fixed digits after decimal
print(f'{1e6 * math.pi:e}')    # exponent notation
print(f'{"hello world":>20}')  # right justify with space filler
print(f'{"hello world":.>20}') # right justify with dot filler
print(f'{20:<10} {10}')        # left justify

"""

alphabet = 'abcdefghijklmnopqrstuvwxyz'

# for i in range(1, len(alphabet)+1):
    # print(len(alphabet)-(i-1), alphabet[-i]) # negative indexing for backword counting

# for i in alphabet:
    # print(i, end='') #end removes spacing

# print(alphabet[4:6]) #prints 4,5 from string
# print(alphabet[:10]) #first 10
# print(alphabet[10:]) #everything after chr 10

# print(s, s[::], s[::1], s[::-1]) # first three are the same, last one inverse order

# for i, nt in enumerate(alphabet): #enumerate is a tuple for indices and values
    # print(i + 1, nt)

nts = 'sdrblcy'
names = ('sam', 'dam', 'ram', 'bam', 'lam', 'cam', 'yam')
six = '123456'

# for nt, name in zip(nts, names): # index a tuple and a string
    # print(nt, name)

# for nt, num in zip(nts, six): # index a string and a string, index w/ lowest index ie: six only has 6 so yam is left out
    # print(nt, num)

# for i, (nt, name) in enumerate(zip(nts, names)): # index + the indexed tuple + string
    # print(i + 1, nt, name)

###
# Lists

ex1 = ['A', 'T', 'C', 'D'] #square brackets instead, they are mutable
# print(ex1[2])
ex1[2] = 'T'
# print(ex1[2])

ex1.append('G') #add to end of list
# print(ex1)

g = ex1.pop() # remove last item of list
# print(g, ex1)


#sort list but not it tuples
ex1.sort()
#print(ex1)
ex1.sort(reverse=True)
#print(ex1)

ex2 = ex1
ex2.append('C')
ex2.sort()
#print(ex1, ex2)

#both ex2 and ex1 get affected

ex3 = list.copy(ex2) # basic 1 dimensional copy
#print(ex3)

a = [] # make a list 
# or 
b = list()

# list can also turn a string into a list

d = list()
# print(c, d)



text = 'good day          to you'
words = text.split() #splits using space like delimiter
#print(words)

line = '1.41,2.72,3.14'
#print(line.split(',')) #split using ,

s = '-'.join(words) # list to string with - as delim
#print(s)
s = ''.join(words) # list to string with nothing as delim (probably not preferred)
#print(s)



alph = 'abcdefghijklmnopqrstuvwxyz'

alphlist = list(alph)

"""

print(alphlist)
print(alphlist)

if 'A' in alph: print('yay') # use 'in' for alpha
if 'a' in alph: print('no')

print('index G?', alphlist.index('g')) #index finds the index: note returns error if not found
print('index Z?', alphlist.index('z'))

print('index G?', alph.index('g')) #index finds the index: note returns error if not found
print('index Z?', alph.index('z'))


print('find G?', alph.find('G')) #for strings: find the index 
print('find Z?', alph.find('Z'))

"""

#practice probx`lems


def minlist(list):
    low = list[0]
    for item in list:
        if item < low: 
            low = item
    return low

def minplusmax(list):
    lo = list[0]
    hi = list[0]
    for item in list:
        if item > hi:
            hi = item
        if item < lo:
            lo = item
    return lo, hi

def meanlist(list):
    tot = 0
    for item in list:
        tot += float(item)
    return tot / len(list)

def entropylist(probs):
    h = 0
    for p in probs:
          h -= p * math.log2(p)
    return h


def kldistance(P, Q):
    tot = 0
    for p, q in zip(P, Q):
        tot += p * math.log2(p / q)
    return tot

#COMMAND LINE

import sys

#print(sys.argv)
#print(sys.argv[0]) # returns program name
#print(sys.argv[1]) # returns first object
#print(sys.argv[2]) # returns second object

print(float('123.123')) #converts string to flaot
print(int('12')) #converts string to int

###
#Pairwise comparisons

"""

for i in range(0, len(list)):
    for j in range(i+1, len(list)):
        print('half matrix w/o diagonal')

"""

