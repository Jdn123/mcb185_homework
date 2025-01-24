def mean3(a, b, c): 
	sum = a+b+c
	return sum/3

print(mean3(5, 6, 7))

def harmonicmean(a, b, c):
	n = 3
	sum = (1/a) + (1/b) + (1/c)
	return n/sum

print(harmonicmean(5, 6, 7))

def diffmean(a, b, c):
	harmonic = harmonicmean(a,b,c)
	mean = mean3(a,b,c)
	return abs(mean - harmonic)

print(diffmean(5,6,7))
