import sys

lines = open(sys.argv[1])

for line in lines:
	maxSub = ""
	lenSub = 0
	first = line.split(";")[0].upper()
	second = line.strip().split(";")[1].upper()
	freqa = [0] * 26
	freqb = [0] * 26
	
	for l in first:
		freqa[ord(l) - ord("A")] += 1
	for l in second:
		freqb[ord(l) - ord("A")] += 1

	for i in range(26):
		if freqa[i] == 0 or freqb[i] == 0:
			first = first.replace(chr(ord("A" + i)), "")
			second = second.replace(chr(ord("A" + i)), "")

	for i in range(len(first)):
		for j in range(len(second)):
			x = 0
			while first[i+x] == second[j+x]:
				x += 1
				if i+x > len(first) - 1 or j+x > len(second) - 1:
					break
				print i, j, x
			if x > lenSub:
				lenSub = x
				maxSub = first[i:i+x]

	print maxSub