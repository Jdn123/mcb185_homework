import sequence
import sys

seq = sys.argv[1]
w = sys.argv[2]


seq1 = 'ACGTACGTGGGGGACGTACGTCCCCC'
g = 10


og = seq1[0:g]
print(0, sequence.gc_comp(og), sequence.gc_skw(og))

x = 1
for i in range(0, len(seq1) - g + 1, 1):
    s1 = seq1[g : g + i]

    s2 = seq[i: i+1]


    print(x, sequence.gc_comp(s), sequence.gc_skw(s))
    x += 1

