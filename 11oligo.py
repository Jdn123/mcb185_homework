def oligomp(a, t, g, c):
    totbp = (a+t+g+c) # number of bp in 1 strand of the oligo nucleotide
    if totbp <= 13: return (a+t)*2 + (g+c)*4
    return 64.9 + 41*(g+c-16.4) / (totbp) 

print(oligomp(1,2,5,5))
print(oligomp(1,2,5,6))