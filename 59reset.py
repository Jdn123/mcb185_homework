import sys
import mcb185

min_nt = int(sys.argv[2])

complement = {'A': 'T', 'G': 'C', 'C': 'G', 'T': 'A'}
stp = ['TAA', 'TAG', 'TGA', 'TRA', 'TAR']

def threeframe(seq):
    three = []
    for i in range(3):
        three.append(seq[i:])
    return three

def revseq(seq):
    rev = seq[::-1]
    revsq = ''

    for nt in rev:
        if nt in complement.keys():
            revsq += complement[nt]
        else:
            revsq += 'X'
    return revsq #returns 5' to 3'

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    print(defline)

    frames = threeframe(revseq(seq))
    total = {}

    lng = len(seq)

    for i, frame in enumerate(frames):
        print(i)

        store = [0, 0]
        col = False
        first = 0
        for j in range(0, len(frame) - 3 + 1, 3):
            codon = frame[j:j+3]

            if codon == 'ATG':
                #print('start', lng - j - i)
                
                if first == 0:
                    store[0] = lng - j - i
                first = 1
                #print(store, 'A')
                col = True

            if codon in stp and col == True:
                #print('stop', lng - j - i + -2)

                first = 0
                store[1] = lng - j - i + -2
                if store[0] - store[1] > min_nt:
                    #print(store)
                    total[store[1]] = store[0]
                    store = [0,0]
                col = False
                
    for k, v in sorted(total.items()):
        print(k, v)
        None

"""
CDS     190     255     +
CDS     337     2799    +
CDS     2801    3733    +
CDS     3734    5020    +
CDS     5234    5530    +
CDS     5683    6459    -
CDS     6529    7959    -
CDS     8238    9191    +
CDS     9306    9893    +
CDS     9928    10494   -
CDS     10643   11356   -
CDS     10830   11315   +
CDS     11382   11786   -
CDS     12163   14079   +
CDS     14168   15298   +
CDS     15445   16557   +
CDS     16751   16960   -
CDS     16751   16903   -
CDS     17489   18655   +
CDS     18715   19620   +


"""