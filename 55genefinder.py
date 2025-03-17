import mcb185
import sys

orf_min = int(sys.argv[2])

complement = {'A': 'T', 'G': 'C', 'C': 'G', 'T': 'A'}

def revseq(seq):
    rev = seq[::-1]
    revsq = ''

    for nt in rev:
        if nt in complement.keys():
            revsq += complement[nt]
        else:
            revsq += 'X'
    return revsq #returns 5' to 3'

def threeframe(seq):
    three = []

    for i in range(3):
        three.append(seq[i:])

    return three

stp = ['TAA', 'TAG', 'TGA', 'TRA', 'TAR']

def cds_index(seq, strand): #strand: True is +, False is -
    cords = {}
    frames = threeframe(seq)
    lng = len(seq)

    if strand:
        for i, frame in enumerate(frames):
            store = [0, 0]
            col = False
            first = 0

            for j in range(0, len(frame) - 3 + 1, 3):
                codon = frame[j:j+3]
                if codon == 'ATG':
                    
                    if first == 0:
                        store[0] = j + i + 1
                    first = 1

                    col = True

                if codon in stp and col == True:

                    first = 0
                    store[1] = j + i + 3
                    if store[1] - store[0] > orf_min:

                        cords[store[0]] = store[1]
                        store = [0,0]
                    col = False

    else:
        for i, frame in enumerate(frames):
            store = [0, 0]
            col = False
            first = 0

            for j in range(0, len(frame) - 3 + 1, 3):
                codon = frame[j:j+3]

                if codon == 'ATG':
                    if first == 0:
                        store[0] = lng - j - i
                    first = 1
                    col = True

                if codon in stp and col == True:
                    first = 0
                    store[1] = lng - j - i + -2
                    if store[0] - store[1] > orf_min:
                        #print(store)
                        cords[store[1]] = store[0]
                        store = [0,0]
                    col = False

    return cords

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    #print(defline)

    #print(len(seq[0:3000]))

    rev = revseq(seq)

    #print(threeframe(seq))
    pos = cds_index(seq, True)
    for key, val in sorted(pos.items()):
        print('CDS', key, val, sep='\t')


    #print(threeframe(rev))
    neg = cds_index(rev, False)
    for key, val in sorted(neg.items()):
        print('CDS', key, val, sep='\t')

    #print(pos, neg)

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
"""

for val, pro in pros.items():
            if pro != '':
                all_pros[val] = pro

                



    for i, frame in enumerate(frames): #only three
        #print(i, frame)
        tran = mcb185.translate(frame)
        #print(seq)

        keep = False
        m_count = 0
        beg = 0
        end = 0
        for j, nt in enumerate(tran):
            if nt == 'M':
                keep = True
                m_count += 1
                if m_count == 1:
                    beg = j

            if nt == '*':
                end = j
                keep = False

            print(beg, end, m_count)
            if keep == False and m_count > 0:

                if strand:
                    #print(beg, end)
                    pros[beg*3 +i] = end*3 + i + 3    
                else:
                    #print(beg, end)
                    pros[lng - end*3 - i] = lng- (beg)*3 -i
                beg = 0 
                end = 0 
                m_count = 0    for i, frame in enumerate(frames): #only three
        #print(i, frame)
        tran = mcb185.translate(frame)
        #print(seq)

        keep = False
        m_count = 0
        beg = 0
        end = 0
        for j, nt in enumerate(tran):
            if nt == 'M':
                keep = True
                m_count += 1
                if m_count == 1:
                    beg = j

            if nt == '*':
                end = j
                keep = False

            print(beg, end, m_count)
            if keep == False and m_count > 0:

                if strand:
                    #print(beg, end)
                    pros[beg*3 +i] = end*3 + i + 3    
                else:
                    #print(beg, end)
                    pros[lng - end*3 - i] = lng- (beg)*3 -i
                beg = 0 
                end = 0 
                m_count = 0

                

pos = cds_index(seq, True)
    for key, val in sorted(pos.items()):
        #print('CDS', key, val, sep='\t')
        None
    
    #minus
    minu = cds_index(rev, False)
    for key, val in sorted(minu.items()):
        #print('CDS', key, val, sep='\t')
        None

def cds_index(seq, strand): #strand: True is +, False is -
    cords = {}
    frames = threeframe(seq)
    lng = len(seq)

    if strand:
        for i, f in enumerate(frames):
            beg = 0
            end = 0
            col = True

            for j in range(0, len(f) - 3 + 1, 3):
                codon = f[j:j+3]
                if codon == 'ATG':
                    beg = j + i + 1
                    col = True
                if codon in stp and col == True:
                    end = j + i + 3   
                    cords[beg] = end
                    col = False

    else:
        for i, f in enumerate(frames):
            beg = 0
            end = 0
            col = True
            
            for j in range(0, len(f) - 3 + 1, 3):
                codon = f[j:j+3]
                if codon == 'ATG':
                    end = lng - i - j
                    col = True
                if codon in stp and col == True:
                    beg = lng - i - j - 2
                    cords[beg] = end
                    col = False

    return cords
        
        
"""



