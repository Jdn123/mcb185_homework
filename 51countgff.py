import sys, gzip


count = {}
with gzip.open(sys.argv[1], 'rt') as fp:
    for line in fp:
        if line.startswith('#'): continue
        f = line.split()

        feature = f[2]
        """ #alternative way of doing
        if feature not in count:    count[feature] = 1
        else:                       count[feature] += 1

        """
        count[feature] = count.get(feature, 0) + 1  # Simplified line for counting
        

for f, n in count.items():
    print(f, n)

"""
region 1
gene 4494
CDS 4337
mobile_genetic_element 50
ncRNA 99
exon 207
rRNA 22
tRNA 86
pseudogene 145
sequence_feature 48
origin_of_replication 1

"""