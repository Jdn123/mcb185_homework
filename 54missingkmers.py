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



for defline, seq in mcb185.read_fasta(sys.argv[1]):
    sqs = []
    sqs.append(seq)
    sqs.append(revseq(seq))

    missing = []
    #print(sqs)

    loop = True
    k = 1
    while loop:
        print(k)
        count = 0
        
        #print(cmbs)
        found = {}
        for sq in sqs:
            for i in range(len(seq) -k +1):
                kmer = sq[i:i+k]
                #print(kmer)
                if kmer in found:   found[kmer] += 1
                else:               found[kmer] = 1
        
        if len(found) == 4 ** k:
            k += 1
            continue
        
        for nt in itertools.product('ACGT', repeat=k):
            kmer = ''.join(nt)
            if kmer not in found:   
                print(kmer)
                count += 1
        
        break
    
    #print(defline)
    print(k, count)