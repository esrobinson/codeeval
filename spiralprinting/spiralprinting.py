import sys

lines = open(sys.argv[1])

for line in lines:
	line = line.strip().split(" ")
	params = line.pop(0).split(";")
	n = int(params[0])
	m = int(params[1])
	numbers = []
	numbers.append(params[2])
	numbers[1:] = line[0:]
	spiral = []
	j = 0
	direct = 0
	rot = 0
	for i in range(n*m):
		spiral.append(numbers[j])
		if direct == 0:
			j += 1
			if j % m == m - rot - 1:
				direct = 1
		elif direct == 1:
			j += m
			if j / m == n - rot - 1:
				direct = 2
		elif direct == 2:
			j -= 1
			if j % m == rot:
				direct = 3
		elif direct == 3:
			j -= m
			if j / m == rot + 1:
				rot += 1
				direct = 0

	print " ".join(spiral)