import sys

# WON'T WORK WITH STRING CONTAINING DUPLICATE LETTERS RIGHT NOW

def permute(letters, s):
	global hackycommaflag
	if len(letters) == 1:
		sys.stdout.write("".join(s+letters))
		#Really ugly check to see if this is the last permutation
		t = sorted(s+letters)
		t.reverse()
		if list(s+letters) != t:
			sys.stdout.write(",")
	else:
		for i in range(len(letters)):
			temp = list(letters)
			l = temp.pop(i)
			permute(temp, s+list(l))

lines = open(sys.argv[1])

for line in lines:
	word = line.strip()
	letters = sorted(list(word))
	permute(letters, [])
	sys.stdout.write("\n")