import sys

lines = open(sys.argv[1])

for line in lines:
	data = line.strip().split(",")
	x = int(data[0])
	n = int(data[1])
	while n < x :
		n *= 2
	print n