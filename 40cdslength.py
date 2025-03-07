import gzip
import sys

with gzip.open(sys.argv[1], 'rt') as fp:
    for line in fp:
        if line[0] != '#':
            words = line.split() # make substrings from a string using a delimitor of ' ' as default
            if words[2] == 'CDS': # find all lines with cds
                beg = int(words[3])
                end = int(words[4])
                print(end - beg + 1)

# prints the number of words in each line beggining with CDS

# python3 40cdslength.py ../MCB185/data/GCF_000005845.2_ASM584v2_genomic.gff.gz > random.sh
# can copy output of this file into a random.sh


# continue statement is used to 'skip' a 'line' in a loop

with gzip.open(sys.argv[1], 'rt') as fp:
    for line in fp:
        if line[0] == '#': continue
        words = line.split()
        if words[2] != 'CDS': continue
        beg = int(words[3])
        end = int(words[4])
        print(end - beg + 1)