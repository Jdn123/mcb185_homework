import sys

colorfile = sys.argv[1]

target = [0,0,0]
target[0] = int(sys.argv[2])
target[1] = int(sys.argv[3])
target[2] = int(sys.argv[4])

########################################

def dtc(D, Q): #calc distance #modify P
    P = D.split(',')
    #print(P, '1')

    d = 0
    for p, q in zip(P, Q):
        d += abs(int(p) - q)
    return d

########################################

with open(colorfile, 'rt') as fp: #create list of only RGB values
    cols = []
    colors = []
    
    for line in fp:
        cols.append(line.split()[2])
        colors.append(line.split()[0])
    #print(cols)

########################################

idx = 0 # index of lowest number
low = 10000 #massive inital low so first idx is always lower and will be initialized
for i, col in enumerate(cols):

    #print(col)
    P = col.split(',')
    #print(P)

    if dtc(col, target) < low:
        low = dtc(col, target)
        idx = i

print(colors[idx], cols[idx])

