import sys

def genDFA(pat):
	dfa =  [[0 for i in range(256)] for j in range(len(pat))]
	x = 0
	dfa[0][ord(pat[0])] = 1
	for i in range(1, len(pat)):
		dfa[i] = dfa[x]
		dfa[i][ord(pat[i])] = i + 1
		x = dfa[x][ord(pat[i])]
	return dfa


lines = open(sys.argv[1])

for line in lines:
	line = line.strip().split(",")
	s = line[0].replace("*", "&")
	pats = line[1].replace("\*", "&").split("*")
	
	i = 0
	j = 0


	while i < len(pats) and len(pats[i]) == 0:
		i += 1
	if i == len(pats):
		print "true"
	else:
		dfa =  genDFA(pats[i])
		for l in s:
			j = dfa[j][ord(l)]
			if j == len(pats[i]):
				i += 1
				while i < len(pats) and len(pats[i]) == 0:
					i += 1
				if i == len(pats):
					print "true"
					break
				else:
					dfa = genDFA(pats[i])
					j = 0
		else:
			print "false"

