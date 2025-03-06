import gzip
import sys
import mcb185


"""

#inint
filepath = sys.argv[1]
fp = gzip.open(filepath, 'rt')

total_len = 0
num_exons = 0

#loop
for line in fp:
    cols = line.split()

    if cols[2] == 'exon': 
        beg = int(cols[3])
        end = int(cols[4])
        total_len += end - beg + 1
        num_exons += 1

#print
# print(total_len/num_exons)

#python3 demo.py ../../MCB185/data/C.elegans.gff.gz

filepath = sys.argv[1]

with gzip.open(filepath, 'rt') as fp:
    for line in fp:
        f = line.split()
        # print(f[3], f[4])



k = 4
seq = 'CATGCGATCGATGATCAGAGTGTACCA'

for i in range(len(seq)):
    kmer = seq[i:i+k]
    if len(kmer) == 4:      print(kmer)


filepath = sys.argv[1]

exons = 0
total = 0

with gzip.open(filepath, 'rt') as fp:
    for line in fp:
        f = line.split()
        if f[2] != 'exon': continue
        beg = int(f[3])
        end = int(f[4])
        total += end - beg + 1
        exons += 1
        # print(f[3], f[4])




filepath = sys.argv[1]

lengths = []

for defline, seq in mcb185.read_fasta(filepath):
    lengths.append(len(seq))

print(lengths)

total = 0
for length in lengths: total += length
print(total / len(lengths))

"""


