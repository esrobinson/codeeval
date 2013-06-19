


class Grid:
	size = None
	root = None
	accessible = None
	N = None

	def __init__(self, limit):
		"""
		Given a limit, set up a grid.

		We find the furthest the monkey could travel in one direction, N, and
		set up a grid from (-N, -N) to (N, N).  Each point starts with size 1,
		is the root of its own tree and is inaccessible.
		"""
		i = 0
		while sumDigits(i, 0) <= limit:
			self.N = i
			i += 1
		self.size = [1 for i in range((2*self.N + 1) ** 2)]
		self.root = [i for i in range((2*self.N + 1) ** 2)]
		self.accessible = [False for i in range((2*self.N + 1) ** 2)]

	def makeAccessible(self, x, y):
		"""
		Marks a point (x, y) as accessible
		and connects it to adjacent accessible points.
		"""
		i = self.getIndex(x, y)
		self.accessible[i] = True
		if x > -self.N and self.isAccessible(x - 1, y):
			self.connect(i, self.getIndex(x - 1, y));
		if y > -self.N and self.isAccessible(x, y - 1):
			self.connect(i, self.getIndex(x, y - 1))

	def connect(self, i, j):
		""" Connects two points.

		Given the indicies of two points, set the root of the smaller
		tree to the root of the larger one.
		"""
		i = self.getRoot(i)
		j = self.getRoot(j)
		if i == j:
			return
		elif self.size[i] > self.size[j]:
			self.root[j] = i
			self.size[i] += self.size[j]
		else:
			self.root[i] = j
			self.size[j] += self.size[i]

	def getRoot(self, i):
		""" Given an index, return the root of the tree containing it."""
		while self.root[i] != i:
			i = self.root[i]
		return i

	def isAccessible(self, x, y):
		return self.accessible[self.getIndex(x, y)]

	def getIndex(self, x, y):
		""" Given a point (x, y), return the index corresponding to it."""
		return (2*self.N + 1)*(y + self.N) + (x + self.N)

def sumDigits(x, y):
	""" 
	Given a point (x, y), return the sum of the digits of the coordinates
	"""
	s = 0
	x = abs(x)
	y = abs(y)
	while x > 0:
		s += x % 10
		x /= 10
	while y > 0:
		s += y % 10
		y /= 10
	return s

LIMIT = 19  #This is the largest sum that our monkey can access

g = Grid(LIMIT)

for y in range(-g.N, g.N + 1):
	for x in range(-g.N, g.N + 1):  #Loop through the entire grid
		if sumDigits(x, y) <= LIMIT:
			g.makeAccessible(x, y)

print g.size[g.getRoot(g.getIndex(0, 0))] #Print the size (0, 0)'s tree

