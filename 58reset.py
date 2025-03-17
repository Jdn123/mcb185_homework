import sys
import mcb185

min_nt = int(sys.argv[2])

stp = ['TAA', 'TAG', 'TGA', 'TRA', 'TAR']

def threeframe(seq):
    three = []
    for i in range(3):
        three.append(seq[i:])
    return three

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    print(defline)

    #print(seq[189:192])

    #print(l1)
    frames = threeframe(seq)
    #print(frames)

    total = {}

    for i, frame in enumerate(frames):
        print(i)

        
        store = [0, 0]
        col = False
        first = 0
        for j in range(0, len(frame) - 3 + 1, 3):
            codon = frame[j:j+3]
            #print(codon)
            if codon == 'ATG':
                print('start', j + i + 1)
                
                if first == 0:
                    store[0] = j + i + 1
                first = 1
                #print(store, 'A')
                col = True

            if codon in stp and col == True:
                print('stop', j + i + 3)

                first = 0
                store[1] = j + i + 3
                if store[1] - store[0] > min_nt:
                    #print(store)
                    total[store[0]] = store[1]
                    store = [0,0]
                col = False
                
    for k, v in sorted(total.items()):
        print(k, v)

"""

CDS     190     255     + ***
CDS     337     2799    +
CDS     2801    3733    +
CDS     3734    5020    +
CDS     5234    5530    + ***
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
CDS     16751   16960   - ***
CDS     16751   16903   - ***
CDS     17489   18655   +
CDS     18715   19620   +


"""


    