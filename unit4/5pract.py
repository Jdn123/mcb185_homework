import sys
import mcb185


gc = 0
lng = 0

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    sq_gc = 0
    print(defline, '\t', sep='',end='')
    lng += len(seq)
    for nt in seq:
        if nt == 'G' or nt == 'C':
            gc += 1
            sq_gc += 1
    print(sq_gc / len(seq))
print('all sequences:', '\t', gc/lng, sep='')

