import sys

class juggler:

	h = None
	e = None
	p = None
	pref = None
	number = None

	def __init__(self, data):
		data = data.split(" ")
		self.number = int(data[1][1:])
		self.h = int(data[2][2:])
		self.e = int(data[3][2:])
		self.p = int(data[4][2:])
		self.pref = [int(i[1:]) for i in data[5].strip().split(",")]

class circut:

	jugglers = []
	number = None
	h = None
	e = None
	p = None

	def __init__(self, data):
		data = data.split(" ")
		self.number = int(data[1][1:])
		self.h = int(data[2][2:])
		self.e = int(data[3][2:])
		self.p = int(data[4][2:])

	def size(self):
		return len(self.jugglers)

lines = open(sys.argv[1])

jugglers = []
circuts = []

for line in lines:
	if line[0] == "C":
		circuts.append(circut(line))
	elif line[0] == "J":
		circuts.append(juggler(line))

N = len(circuts)
M = len(jugglers)

teamSize = M/N

for juggler in jugglers:
	