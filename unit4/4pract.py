import sys

target = [0,0,0]
target[0] = sys.argv[2]
target[1] = sys.argv[3]
target[2] = sys.argv[4]

def dtc(P, Q):
	d = 0
	for p, q in zip(P, Q):
		d += abs(int(p) - int(q))
	return d

def dist(P, Q):
    d = 0
    for p, q in zip(P, Q):
        d += (int(p) - int(q)) ** 2
    return d ** .5

with open(sys.argv[1]) as fp:
    color = ''
    least = 1000000
    value = []

    for line in fp:
        #print(line)
        #print(line.split())
        cols = line.split() #split into color, hex, and RBG
        #print(cols)
        #print(cols[2])
        #print(cols[0])

        RGB = cols[2].split(',')
        #print(RGB)

        d = dtc( RGB, target)
        #print(d)
        #print(i)

        if d < least:
            least = d
            color = cols[0]
            value = RGB

print(color, ','.join(value))




        

        