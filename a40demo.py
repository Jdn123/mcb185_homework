###UNIT 4###

import gzip #
import sys

"""

import gzip
with gzip.open(path, 'rt') as fp:
    do_something

    
original
with open(path) as fp:
    do_something

"""

for defline, seq in mcb185.read_fasta(arg.fasta):
    mask = ''
    for i in range(len.....):
        win = seq[]
        if entropy(win) > x:
            winstr = ''
            for j in range(i, i+arg.size):
                winstr += 'N'


            if(g < 1):
                mask += seq[0:i] + winstr
            else:
                mask += mask[0:i] + winstr
            g += 1

    if len(mask) < len(seq): # 5 - 7 = 2
        #01234 0123456
        g = len(seq) - len(mask)
        mask += seq[len(seq)-g:len(seq)]

    if len(mask) == 0:      print(seq)
    else:                   print(mask)



