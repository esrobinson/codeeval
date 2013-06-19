import math
import sys

lines = open(sys.argv[1])
N = int(lines.readline())

for line in lines:
	nsums = 0
	i = 0
	if line.strip() != '':
		num = int(line)
		while i**2 < num / 2:
			if int(math.sqrt(num - i**2)+0.5)**2 == num - i**2:
				nsums += 1
			i +=1
		if num == 0 or num == 1:
			nsums = 1
		print nsums