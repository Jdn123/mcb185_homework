import sys
import mcb185

comps = []
tot_ln = 0
for defline, seq in mcb185.read_fasta(sys.argv[1]):
    defwords = defline.split() #splits identifier into a list: Chr #, and BP range
    #print(defwords)

    name = defwords[0] #chr name

    gc = 0 # total number of g/c

    #print(type(seq)) #note seq is a string
    tot_ln += len(seq)

    # use a string
    #remember you can iterate through both strings and list, just can't modify strings
    for nt in seq:
        if nt == 'G' or nt == 'C': 
            gc += 1
    comps.append(gc)

    print(name, gc/len(seq))

tot_comp = 0
for comp in comps:
    tot_comp += comp

print('total composition: ',tot_comp/tot_ln)



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