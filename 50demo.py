s = {'T'}

#print(s)

s.add('A') #need to add something into set before using any of its functions

#print(s) 

ls = ['A', 'T', 'G', 'C']

#s.add(ls) only add strings into a set

for l in ls:
    s.add(l)

#print(s) #prints stuff in set at random orders

s1 = {'A', 'T', 'G', 'P'}

for char in s:
    if char in s1:
        #print('1')
        None

# fast way to compare two sets

dit = {} 
dit = dict() #make a dictionary

dit = {'dog': 'woof', 'cat': 'meow'} # key: value
#print(dit)

#print(dit['dog']) #woof

dit['pig'] = 'oink' #add new keys and values to a dictionary
#print(dit['pig'])

dit['pig'] = 'oinkk' #modify a key
#print(dit['pig'])

del dit['pig'] #delete a key:value pair
#print(dit)

if 'cat' in dit: #find a key in a dictionary
    #print(dit['cat'])
    None

##Iteration: 2 ways

for key in dit:
    #print(f'{key}, {dit[key]}')
    None

for k, v in dit.items():
    #print(k, v)
    None

print(dit.keys(),                           #print only the keys 
      dit.values(),                         #print only the values
      list(dit.values()))                   #makes a list of the values


kdtable = {
    'I':  4.5, 'V':  4.2, 'L':  3.8, 'F':  2.8, 'C':  2.5, 'M': 1.9, 'A': 1.8,
    'G': -0.4, 'T': -0.7, 'S': -0.8, 'W': -0.9, 'Y': -1.3, 'P':-1.6, 'H': -3.2,
    'E': -3.5, 'Q': -3.5, 'D': -3.5, 'N': -3.5, 'K': -3.9, 'R': -4.5
}

def kd_dict(seq):
    kd = 0
    for aa in seq: kd += kdtable[aa]
    return kd/len(seq)
#much simpler than comparing two parallel lists


def nt_comp(seq):
    count = {}
    for nt in seq:
        if nt not in count: count[nt] = 0
        count[nt] += 1

    return count


seq = 'ATGATGATGATGGCGCGCGAAA'
comp = nt_comp(seq) 

for nt in sorted(comp): #sort by keys
    #print(nt, comp[nt])
    None



for k, v in sorted(comp.items(), key=lambda item: item[1]): #sort by values
    #print(k, v)
    None


def by_value(tuple):
    return tuple[1]

for k, v in sorted(comp.items(), key=by_value): #by value makes it sort by value
    #print(k, v)
    None

import itertools
for nts in itertools.product('ACGT', repeat=2):
    #print(nts)
    None