import sys

lines = open(sys.argv[1])

for line in lines:
	data = line.strip().split(" ")
	prefixes = []
	numbers = []
	while data[0] == "*" or data[0] == "+" or data[0] == "/":
		prefixes.append(data.pop(0))
	for number in data:
		numbers.append(int(number))
	for operation in reversed(prefixes):
		if operation == "*":
			numbers[0] = numbers.pop(0) * numbers[0]
		elif operation == "+":
			numbers[0] = numbers.pop(0) + numbers[0]
		elif operation == "/":
			numbers[0] = numbers.pop(0) / numbers[0]
	print numbers[0]
