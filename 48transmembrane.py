import sys
import mcb185

let = [
    "I", "V", "L", "F", "C", "M", "A", "G", "T", "S", "W", "Y", "P", 
    "H", "E", "Q", "D", "N", "K", "R"]

phobs = [
    4.5, 4.2, 3.8, 2.8, 2.5, 1.9, 1.8, -0.4, -0.7, -0.8, -0.9, -1.3, 
    -1.6, -3.2, -3.5, -3.5, -3.5, -3.5, -3.9, -4.5]

def kd(seq): #only calculating hydrophobicity
    tot = 0
    for nt in seq:
        if nt in let:
            tot += phobs[let.index(nt)]
    return tot / len(seq)


def is_tag(seq, thres, win):
    kd_val = 0

    #loc : N or C

    #print(sq)
    #print(type(sq))
    #print(len(sq))
    #sliding window to search for a tag
    for i in range(0, len(seq) - win + 1, 1):
        #print(i)
        #print(sq[i:i+win])
        sl = seq[i:i+win]
        kd_val = kd(sl)
        if kd_val >= thres and 'P' not in sl: #must meet hydrophobicity + proline requirement
            return True
    
    return False

x = 0
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    #print(seq)
    #print(defline, '\n', seq)

    signal = is_tag(seq[0:30], 2.5, 8)
    trans = is_tag(seq[30:], 2.0, 11)

    if signal == True and trans == True:
        print(defline)
        x += 1
                    
print(x) #468- proteins
            
    



"""
    for i in range(0, len(Nterm)-8+1, 1):
        if kd(Nterm[i:i+8]) >= 2.5:
            signal = True

    for i in range(0, len(Cterm)-11+1, 1):
        if kd(Cterm[i:i+11]) >= 2.0:
            trans = True 
"""




#print(kd('MKKTAAGGCTAGGAGGTAGGAGGAGGGAGGAGGAGGAGGAGGGGAG'))



"""
seq = 'MKKTAAGGCTAGGAGGTAGGAGGAGGGAGGAGGAGGAGGAGGGGAG'

tot = 0
for nt in seq:
    if nt in aas:
        idx = aas.index(nt)
        #print(idx)
        tot += phobs[idx]

"""


"""
aas = []
defline = []

#print(aa, defline)

with gzip.open(sys.argv[1], 'rt') as fp:
    #print(fp.read()) #string
    #print('placeholder')
    #print(fp.read().split()[])
    #print()

    cont = 0 
    i = 0


    seq = ''
    for f in fp:
        if f.count('>') != 0:
            defline.append(f)
            cont = 0
            seq = ''
            i += 1

        else:
            cont += 1
            if cont > 0:
                seq += f
            
        sqs = list(seq)
        #print(seq)
        if seq != '':
            for j, sq in enumerate(sqs):
                if sq ==  '\n':
                    sqs[j] = ''
            #print(sqs)
            per.append(''.join(sqs))

        
        if len(defline) > len(aas):
            aas.append(sqs)

    
#print(len(defline))
#print(len(aas))
#print(aas)

#print('1')

for line, aa in zip(defline, aas):

"""