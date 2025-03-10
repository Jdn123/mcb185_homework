def transcribe(dna):
    return dna.replace('T', 'U')
#DNA -> RNA

def revcomp(dna):
    rc =[]
    for nt in dna[::-1]: # read in reverse
        if nt == 'A':   rc.append('T')
        elif nt == 'T': rc.append('A')
        elif nt == 'G': rc.append('C')
        elif nt == 'C': rc.append('G')
        else:           rc.append('N')    #add the complement for the template strand into a list
    return ''.join(rc) #convert list into string

# can be used as an import

#note this the program returns a comp seq in the same orientation as the original strand
# 5-3 for example


###translation

def translate(dna):
    aas = [] #list for amino acids

    for i in range(0, len(dna), 3):
        codon = dna[i:i+3]
        if codon == 'ATG':      aas.append('M')
        elif codon == 'TAA':    aas.append('*')
        elif codon == 'TAG':    aas.append('*')
        elif codon == 'TGA':    aas.append('*')
        else:                   aas.append('X')

    return ''.join(aas)





def translate1(dna):
    g = 0

    for i in range(0, len(dna)): #find index of first ATG start codon
        if dna[i:i+3] == 'ATG':
            g = i

    aas = [] #amino acid list

    for j in range(g, len(dna), 3): #codon iterating loop starting at index of first start codon
        if len(dna[j:]) < 3: # break loop if remaining seq is less than 3
            break


        codon = dna[j:j+3]
        if codon == 'ATG':      aas.append('M')
        elif codon == 'TAA':    aas.append('*');    break #stop at first stop codon
        elif codon == 'TAG':    aas.append('*');    break
        elif codon == 'TGA':    aas.append('*');    break
        else:                   aas.append('X')

    if (''.join(aas)).count('M') == 0:  return 'N/A' # no stop codon, no amino acid sequence
    
    return ''.join(aas)


"""
dna1 = 'ATGAAAAAAAAATAA'
dna2 = 'AATGAAATAA'
dna3 = 'AATGA'
dna4 = 'TAA'
print(translate1(dna1))
print(translate1(dna2))
print(translate1(dna3))
print(translate1(dna4))

"""

def gc_comp(seq):
    return (seq.count('G') + seq.count('C')) / len(seq)

def gc_skw(seq):
    c = seq.count('C')
    g = seq.count('G')
    if c+g == 0: return 0
    return (g-c)/ (g+c)
