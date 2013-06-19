import sys

class Pqueue:

	queue = ['']
	n = 0

	def exch(self, a, b):
		temp = self.queue[a]
		self.queue[a] = self.queue[b]
		self.queue[b] = temp

	def enqueue(self, s):
		self.queue.append(s)
		self.n += 1
		self.swim(self.n)

	def dequeue(self):
		self.exch(1, self.n)
		temp = self.queue.pop()
		self.n -= 1
		self.sink(1)
		return temp

	def swim(self, i):
		if (i > 1):
			if len(self.queue[i]) < len(self.queue[i/2]):
				self.exch(i, i/2)
				self.swim(i/2)

	def sink(self, i):
		if self.n >= 2*i:
			if self.n > 2*i and len(self.queue[2*i+1]) < len(self.queue[2*i]):
				if len(self.queue[2*i+1]) < len(self.queue[i]):
					self.exch(i, 2*i+1)
					self.sink(2*i+1)
			elif len(self.queue[2*i]) < len(self.queue[i]):
				self.exch(i, 2*i)
				self.sink(2*i)

	def len(self):
		return self.n

	def smallLine(self):
		return len(self.queue[1])



lines = open(sys.argv[1])

N = int(lines.readline())

topn = Pqueue()

for line in lines:
	line = line.strip()
	if topn.len() < N:
		topn.enqueue(line)
	elif len(line) > topn.smallLine():
		topn.dequeue()
		topn.enqueue(line)

out = []

while topn.len() > 0:
	out.append(topn.dequeue())

out = reversed(out)

print "\n".join(out)

