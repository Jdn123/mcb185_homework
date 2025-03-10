import sequence


print(sequence.transcribe('ACGT'))
print(sequence.revcomp('AAAACGT'))


s = 'ACGTGGGGGGCATATG'
print(sequence.gc_comp(s))
print(sequence.gc_skw(s), sequence.gc_skw(sequence.revcomp(s)))