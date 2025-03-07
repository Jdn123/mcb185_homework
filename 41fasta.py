import sys
import mcb185


for defline, seq in mcb185.read_fasta(sys.argv[1]):
    #print(defline[:30], seq[:40], len(seq))
    a = 0
    c = 0
    t = 0
    g = 0
    n = 0

    iden = defline.split()
    name = iden[0]

    #print(seq)
    #print(len(seq))
    """
    for nt in seq:
        if nt == 'A':       a += 1
        elif nt == 'C':     c += 1
        elif nt == 'G':     g += 1
        elif nt == 'T':     t += 1
        else:               n += 1

    print(name, a/len(seq), c/len(seq), t/len(seq), g/len(seq), n/len(seq))

    
    counts = [0, 0, 0, 0, 0]
    for nt in seq:
        if nt == 'A':       counts[0] += 1
        elif nt == 'C':     counts[1] += 1
        elif nt == 'G':     counts[2] += 1
        elif nt == 'T':     counts[3] += 1
        else:               counts[4] += 1   
    print(name, counts[0]/len(seq), counts[1]/len(seq), counts[2]/len(seq), counts[3]/len(seq), counts[4]/len(seq))

 


    nts = 'ACGTN'
    counts = [0] * len(nts)
    #same number of items as nts
    for nt in seq:
        idx = nts.find(nt)
        #use the find, find the index of nt in nts
        #print(idx)
        counts[idx] += 1
    print(name, end = ' ')

    for n in counts:
        print(n/len(seq), end=' ')
    print()
    """


    nts = []
    counts = []
    for nt in seq:
        if nt not in nts:
            nts.append(nt)
            counts.append(0)
        #makes nts and counts
        idx = nts.index(nt)
        counts[idx] += 1
    #makes a new nts, counts for each seq

    print(name)
    for nt, n in zip(nts, counts):
        print(nt, n, n/len(seq))
    print()

    



#defline prints identifer
#seq is the actual sequence







