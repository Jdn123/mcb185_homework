import sys

with open(sys.argv[1]) as fp:
    for f in fp:
        print('>', f, sep='', end='')


"""

with open(sys.argv[1]) as fp:
    for f in fp:
        #print(list(f))
        lst = list(f)
        lst.pop()
        print('>', ''.join(lst), sep='')
        #print('>', , sep='')
#each f in fp has a endline

with open(sys.argv[1]) as fp:
    for f in fp:
        #print(list(f))
        lst = list(f)
        print('>', ''.join(lst[0:len(lst)-1]), sep='')
        #print('>', , sep='')
#each f in fp has a endline


with open(sys.argv[1]) as fp:
    for f in fp:
        #print(list(f))
        lst = list(f)
        lst.pop()
        print('>', ''.join(lst), sep='')
        #print('>', , sep='')
#each f in fp has a endline
        


import gzip

with gzip.open(sys.argv[1], 'rt') as fp:
    #print(fp.read()) #string
    #print('placeholder')
    #print(fp.read().split()[])
    #print()

    cont = 0 
    i = 0
    defline =[]
    aas = []

    seq = ''
    for f in fp:
        if f.count('>') != 0:
            defline.append(f)
            cont = 0
            seq = ''
            i += 1

        else:
            cont += 1
            if cont > 0:
                seq += f
            
        sqs = list(seq)
        print(seq)
        for j, sq in enumerate(sqs):
            if sq ==  '\n':
                sqs[j] = ''
        #print(sqs)
        aas.append(''.join(sqs))

#print(defline)
#print(aas)"
""
""
"
"""