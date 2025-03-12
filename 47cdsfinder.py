import sys
import mcb185

least = int(sys.argv[2])

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

"""
def sixtranslate(sq):
    prots = []
    revsq = sq[::-1] #reverse of seq

    seqs = []
    seqs.append(sq)
    seqs.append(revsq)


    for seq in seqs:
       
        for i in range(0, 3): #three frames
            pro = [] # need to empty every loop
            collision = False    

            for j in range(i, len(seq[i:])-3+1, 3):                

                if seq[j:j+3] == 'ATG':
                    frame = j
                    for k in range(frame, len(seq[j:])-3+1, 3):
                        codon = seq[k:k+3]
                        if codon in mcb185.GCODE:
                            pro.append(mcb185.GCODE[codon])
                            if mcb185.GCODE[codon] == '*':
                                collision = True
                                break
                        else:
                            pro.append('X') 
                if collision == True:
                    break           
            
            if len(pro) >= least: #add pro to prots
                a = ''.join(pro)
                prots.append(a)
            else:
                prots.append('')

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


for defline, seq in mcb185.read_fasta(sys.argv[1]):
    prots = sixtranslate1(seq)
    #print(defline)
    #print(prots)

    
    print(defline, '\n', end='')
    for prot in prots:
        if len(prot) > 0:
            print('>', sep ='', end='')
            for i in range(0, len(prot) +1, 60):
                print(prot[i:i+60])
    print()
    
    

