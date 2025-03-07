import sys
import mcb185


for defline, seq in mcb185.read_fasta(sys.argv[1]):
    defwords = defline.split() #splits identifier into a list: Chr #, and BP range
    #print(defwords)

    name = defwords[0] #chr name

    gc = 0 # total number of g/c

    #print(type(seq)) #note seq is a string


    # use a string
    #remember you can iterate through both strings and list, just can't modify strings
    for nt in seq:
        if nt == 'G' or nt == 'C': 
            gc += 1
        
    print(name, gc/len(seq))


"""
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    defwords = defline.split() #splits identifier into a list: Chr #, and BP range
    #print(defwords)

    name = defwords[0] #chr name

    gc = 0 # total number of g/c

    #print(type(seq)) #note seq is a string


    # use a list
    nts = list(seq)

    for nt in nts:
        if nt == 'G' or nt == 'C': 
            gc += 1
        
    print(name, gc/len(seq))


"""