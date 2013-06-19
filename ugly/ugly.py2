import sys

def getNumbers(digits):
	nums = []
	for i in range(2**(len(digits)-1)):
		k = 0
		temp = list(digits)
		for j in reversed(range(len(digits)-1)):
			if i % (2**(j+1)) >= 2**j:
				t = temp.pop(k)
				temp[k] += 10*t
			else: k += 1
		nums.append(temp)
	return nums

def getUglies(start, remaining):
	if len(remaining) == 0:
		if isUgly(start):
			return [start]
		else:
			return []
	else:
		temp = list(remaining)
		n = temp.pop(0)
		a = []
		a += getUglies(start+n, temp)
		a += getUglies(start-n, temp)
		return a

def isUgly(n):
	return n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0

lines = open(sys.argv[1])

for line in lines:
	digits = [int(i) for i in list(line.strip())]
	if len(digits) > 1:
		numbers = getNumbers(digits)
	else: numbers = [digits]
	a = []
	for num in numbers:
		n = num.pop(0)
		a += getUglies(n, num)
	print len(a)


