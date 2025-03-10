import sequence
import sys

seq = sys.argv[1]
w = sys.argv[2]


seq1 = 'ACGTACGTGGGGGACGTACGTCCCCC'
g = 10

print(0, sequence.gc_comp(  seq1[0:g]), sequence.gc_skw( seq1[0:g]))

x = 1
for i in range(g, len(seq1)-g +1, 1):
    s = seq1[i:i+g]
    print(x, sequence.gc_comp(s), sequence.gc_skw(s))
    x += 1

