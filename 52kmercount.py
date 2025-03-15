import sys, mcb185

import itertools



k = int(sys.argv[2]) # length of kmer
kcount = {}
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    for i in range(len(seq) - k + 1):
        kmer = seq[i:i + k]
        if kmer not in kcount: 
            kcount[kmer] = 0
        kcount[kmer] += 1
for kmer, n in kcount.items(): 
    #print(kmer, n)
    None

#print(kcount)

for nts in itertools.product('ACGT', repeat = k):
    str_nts = ''.join(nts)

    if str_nts in kcount:       print(str_nts, kcount[str_nts])
    else:                       print(str_nts, 0)




"""

nts_comb = {}
for nts in itertools.product('ACGT', repeat = k):
    if nts not in nts_comb:
        nts_comb[''.join(nts)] = 0
    nts_comb[''.join(nts)] += 1
    
for comb in nts_comb:
    print(comb)    

"""


    


