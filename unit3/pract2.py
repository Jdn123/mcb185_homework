import sys

mrna = sys.argv[1]



"""
print('position', '\t', 'frame', '\t', 'codon' )
#make the frames
b = 1
for i in range(0, len(mrna)):
    frame = mrna[i:]
    #print(frame)

    #make codons
    g = 1
    for j in range(0, len(frame)+1, 3): # cut by threes
        trunc = frame[j:]
        if len(trunc) >= 3:     
            print(b, '\t', g, '\t', trunc[0:3]) # make sure codon is 3
        else:                   
            break # any less, stop 

        g += 1
    
    b += 1







b = 1
for i in range(1, len(mrna)+1):
    frame = mrna[i:]
    print(b, frame)
    b += 1


frame = mrna[0:]

g = 1
for i in range(0, len(frame), 3):
    print(g, end='  ')
    g += 1
    codon = frame[i:i+3]
    print(codon)




for i in range(len(mrna)):
    #position = i+1
    g = 3

    if len(mrna[i:]) > 2:
        print(i+1, end='\t')

        if i % 3 == 0:      print(1, end='\t') #first three are part of first reading frame  
        elif i % 3 == 1:    print(2, end='\t') #then it moves to next
        else:               print(3, end='\t') #then again,
        #the fourth frame then overlaps with first
        
        codon = mrna[i:i+3]
        print(codon)

    g += 1

    

print('frame', '\t', 'codon #', '\t', 'codon' )
#make the frames
b = 1
for i in range(0, len(mrna)):
    frame = mrna[i:]
    #print(frame)

    #make codons
    g = 1
    for j in range(0, len(frame)+1, 3): # cut by threes
        trunc = frame[j:]
        if len(trunc) >= 3:     
            print(b, '\t', g, '\t', trunc[0:3]) # make sure codon is 3
        else:                   
            break # any less, stop 

        g += 1
    
    b += 1
"""

for i in range(len(mrna)-2):    print(i+1, i%3 + 1, mrna[i:i+3], sep='\t')


print('frame', '\t', 'codon #', '\t', 'codon' )
#make the frames
b = 1
for i in range(0, len(mrna)):
    frame = mrna[i:]
    #print(frame)

    #make codons
    g = 1
    for j in range(0, len(frame)+1, 3): # cut by threes
        trunc = frame[j:]
        if len(trunc) >= 3:     
            print(b, '\t', g, '\t', trunc[0:3]) # make sure codon is 3
        else:                   
            break # any less, stop 

        g += 1
    
    b += 1