import argparse
import mcb185
import math

parser = argparse.ArgumentParser(description='DNA entropy filter.')
#file
parser.add_argument('file', type=str, help='name of fasta file')
#int for window size
parser.add_argument('-s', '--size', type=int, default = 20, help='window size [%(default)i]')
#float for threshold
parser.add_argument('-e', '--entropy', type=float, default = 1.4, help='entropy threshold [%(default).3f)]')
#flag
parser.add_argument('--lower', action='store_true', help='soft mask')

arg = parser.parse_args()
#print('dusting with', arg.file, arg.size, arg.entropy)

def entropy(seq):
    h = 0
    lng = len(seq)
    comp = {}
    
    for nt in seq:
        if nt not in comp:
            comp[nt] = 0
        comp[nt] += 1
    #print(comp)

    for count in comp.values():
        #print(count, type(count))
        prob = count / lng
        h -= prob * math.log2(prob)
    return h


lower = False
if arg.lower:
    lower = True


for defline, seq in mcb185.read_fasta(arg.file):
    #print(defline)
    sq = list(seq)
    
    for i in range(0, len(seq) - arg.size + 1, 1):
        #print(  seq[i:i + arg.size] )
        kmer = seq[i:i + arg.size]
        #print(     entropy(kmer, arg.size)     )
        if entropy(kmer) < arg.entropy:
            #print('A')
        #else: print('B') just for testing
            for j in range(i, i+arg.size):
                if lower == True:       sq[j] = sq[j].lower()
                else:                   sq[j] = 'N'

    #print
    print('>', defline, sep='')
    seq1 = ''.join(sq)
    #print(seq1)
    for i in range(0, len(seq1), 60):
        print(seq1[i:i+60])
 #line delim btw seq


