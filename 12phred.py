import math

def char_to_prob(a):
    phrd = ord(a) - 33
    if phrd < 0 or phrd > 74:
        return None
    return 10 ** (-phrd/10)

print(char_to_prob('9')) #0.003981071705534973, .004 in wiki
# most be a character input

def prob_to_char(a):
    phrd = -10*math.log10(a)
    if (phrd+33) < 33 or (phrd+33) > 74: # alternative use phrd < 0 or phrd > 41
        return None
    return chr( math.ceil(phrd + 33) ) # chr(integer) need to convert to integer: round up

print(prob_to_char(4e-3)) 

print(char_to_prob(':'))
print(prob_to_char(3e-3)) 