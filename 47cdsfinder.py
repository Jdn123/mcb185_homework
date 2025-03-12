import sys
import mcb185

least = int(sys.argv[2])

def six_frame(seq):
    frames = [0,0,0,0,0,0]
    sq = seq
    revsq = seq[::-1]

    sqs = []
    sqs.append(sq)
    sqs.append(revsq)

    count = 0
    for sq in sqs:
        for i in range(3):
            frames[count] = sq[i:]
            count += 1

    return frames
    
def translate1(seq):
    prots =[]

    frame = 0
    for i in range(0, len(seq)-3+1, 3): 
        pro = [] # need to empty every loop

        if seq[i:i+3] == 'ATG':
            frame = i
            for i in range(frame, len(seq)-3+1, 3):
                codon = seq[i:i+3]
                if codon in mcb185.GCODE:
                    pro.append(mcb185.GCODE[codon])
                    if mcb185.GCODE[codon] == '*':
                        break
                else:
                    pro.append('X')            
        
        if len(pro) >= least: #add pro to prots
            a = ''.join(pro)
            prots.append(a)
    return prots



count = 0
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    #defline
    g = defline.split()[0]
    
    frames = six_frame(seq)
    #print(frames)
    
    cds = []

    for frame in frames: 
        prots = translate1(frame)
        #print(prots)
        for pro in prots:
            if pro != []:
                cds.append(pro)

    #print(cds)
    
    for cd in cds:
        print('>', g, '-', 'protein', '-', count, sep='', end='') 
        print( '\n', end='')
        for i in range(0, len(cd) +1, 60):
            print(cd[i:i+60])
        print()
        count += 1
    
    
    






























"""

def translate1(seq):
    prots =[]

    frame = 0
    for i in range(0, len(seq)): #find index of first ATG start codon
        pro = [] # need to empty every loop

        if seq[i:i+3] == 'ATG':
            frame = i
            for i in range(frame, len(seq), 3):
                codon = seq[i:i+3]
                if codon in mcb185.GCODE:
                    pro.append(mcb185.GCODE[codon])
                    if mcb185.GCODE[codon] == '*':
                        break
                else:
                    pro.append('X')            
        
        if len(pro) >= least: #add pro to prots
            a = ''.join(pro)
            prots.append(a)
    return prots


for defline, seq in mcb185.read_fasta(sys.argv[1]):
    prots = translate1(seq)

    print(defline)
    for prot in prots:
        print('>', end='')
        for i in range(0, len(prot) +1, 60):
            print(prot[i:i+60])
    print()


def sixtranslate(sq):
    prots = []
    revsq = sq[::-1] #reverse of seq

    seqs = []
    seqs.append(sq)
    seqs.append(revsq)

    #print(seqs)

    for seq in seqs:
       
        prots = []    

        for i in range(0, 3, 1): #three frames
 
            for j in range(i, len(seq[i:])-3+1, 3):                     
                pro = [] # need to empty every loop  

                
                if seq[j:j+3] == 'ATG':
                    frame = j

                    for k in range(frame, len(seq[j:])-3+1, 3):
                        codon = seq[k:k+3]
                        if codon in mcb185.GCODE:
                            pro.append(mcb185.GCODE[codon])
                            
                            if mcb185.GCODE[codon] == '*':
                                break
                        else:
                            pro.append('X') 
         
                if len(pro) >= least: #add pro to prots
                    a = ''.join(pro)
                    prots.append(a)

    #print(len(prots))
    return prots

def sixtranslate1(sq):
    prots = []
    revsq = sq[::-1] #reverse of seq

    seqs = []
    seqs.append(sq)
    seqs.append(revsq)


    for seq in seqs:
       
        for i in range(0, 3): #three frames    
            
            pro = ''
            idx = ''
            for j in range(i, len(seq[i:])-3+1, 3):                    
                if seq[j:j+3] == 'ATG':
                    pro = mcb185.translate(seq[j:], 0)
                    trans = list(pro)
                    idx = trans.index('*')
                    break     
            
            if len(pro[0:idx]) >= least: #add pro to prots
                prots.append(pro[0:idx])
            else:
                prots.append('')

    #print(len(prots))
    return prots


#sq = 'ATGGGCTAGGTCAGAGGAGAGGCTGACAGCTGACGAGGCTGACGAGGCTGAC'
#print(sixtranslate(sq))


def sixtranslate(sequence):
    seq = sequence
    revseq = sequence[::-1]

    sqs = []

    sqs.append(seq)
    sqs.append(revseq)
    #print(sqs)

    prots = []

    for sq in sqs:
        #rint(len(sq))
        #print('1')
        for i in range(3):
            tran = mcb185.translate(sq[i:])
            #print(tran)

            for j in range(len(tran)):
                sub = tran[j:]
                if sub[0] == 'M' and '*' in sub:
                    idx = sub.index('*')
                    #print(tran[j:idx+1])

                    if len(sub[0:idx]) >= least:
                        prots.append(tran[j:idx+1])
                    else:
                        continue
                else:
                    continue

                print('3')
                print(prots)

            
            if sq[i:i+3] == 'ATG':
                frame = i
                ORF = sq[frame:]
                pro = mcb185.translate(ORF)
                if pro.index('*') > 0:
                    idx = pro.index('*')
                    #print(pro[0:idx+1])
                else:
                    pro = ''

            if len(pro) >= least:
                prots.append(''.join(pro[0:idx+1]))
                               




    return prots


"""


