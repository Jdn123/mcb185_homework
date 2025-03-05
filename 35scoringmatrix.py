import sys


nbases = sys.argv[1]
mat = sys.argv[2]
mismat = sys.argv[3]


bases1 = list(nbases)
bases2 = list(nbases)

#print(bases1, bases2)



print('   ', 'A', 'C', 'G', 'T', '\n', end='')
for bas1 in bases1:

    print(bas1, ' ', end='')

    for bas2 in bases2:
        if bas1 == bas2:    print(mat, end='')
        else:               print(mismat, end='')
    print('\n')
print()


