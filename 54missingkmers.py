import mcb185
import sys
import itertools

complement = {'A': 'T', 'G': 'C', 'C': 'G', 'T': 'A'}
#print(complement)

def revseq(seq):
    rev = seq[::-1]
    revsq = ''

    for nt in rev:
        if nt in complement.keys():
            revsq += complement[nt]
        else:
            revsq += 'X'
    return revsq #returns 5' to 3'

def comb(k):
    combs = {}
    for nt in itertools.product('ACGT', repeat=k):
        cmb = ''.join(nt)
        if cmb not in combs:    combs[cmb] = 0
    return combs

for defline, seq in mcb185.read_fasta(sys.argv[1]):
    sqs = []
    sqs.append(seq)
    sqs.append(revseq(seq))

    missing = []
    #print(sqs)

    loop = True
    k = 1
    while loop:
        count = 0
        cmbs = comb(k)
        #print(cmbs)

        for sq in sqs:
            for i in range(len(seq) -k +1):
                kmer = sq[i:i+k]
                #print(kmer)
                if kmer in cmbs:   cmbs[kmer] += 1
        
        for kmer, cnt in cmbs.items():
            if cnt == 0:
                missing.append(kmer)
                count += 1

        if len(missing) != 0:
            loop = False
        k += 1
    
    #print(defline)
    print(k-1, missing, count)