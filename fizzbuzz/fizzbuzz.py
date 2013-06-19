import sys

lines = open(sys.argv[1])

for line in lines:
    line = line.split(" ")
    A = int(line[0])
    B = int(line[1])
    N = int(line[2])

    for i in range(1, N+1):
        if i % (A*B) == 0:
            sys.stdout.write("FB")
        elif i % A == 0:
            sys.stdout.write("F")
        elif i % B == 0:
            sys.stdout.write("B")
        else:
            sys.stdout.write(str(i))
        if i != N:
            sys.stdout.write(" ")
    sys.stdout.write("\n")