import math

def isPrime(x):
	for i in range(2, int(math.sqrt(x)+1)):
		if x % i == 0:
			return False
	return True

sum = 2

i = 1
j = 3

while i < 1000:
	if isPrime(j):
		sum += j
		i += 1
	j += 2

print(sum)