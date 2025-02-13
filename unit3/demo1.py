
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

for i, (nt, name) in enumerate(zip(nts, names)): # index + the indexed tuple + string
    print(i + 1, nt, name)


