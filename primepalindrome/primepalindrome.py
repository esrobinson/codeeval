import math

def checkPalindromes():
	for i in reversed(range(10)):
		for j in reversed(range(10)):
			if isPrime(i*101+j*10):
				return i*101+j*10

def isPrime(x):
	for i in range(2, int(math.sqrt(x)+1)):
		if x % i == 0:
			return False
	return True

print checkPalindromes()