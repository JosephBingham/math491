
b = dict()

g = ["000", "001", "010", "011", "100", "101", "110", "111"]
for i in g:
	b[i] = 0

a = "101 & 010 & 111 & 100 & 001 & 000 & 101 & 000 & 101 & 110 & 011 & 100 & 101 & 110 & 011 & 100"
a = a.split(" & ")

for i in a:
	b[i] += 1

for i in g:
	print i, b[i]

print "\n\n\n"

b = dict()

g = ["000", "001", "010", "011", "100", "101", "110", "111"]
for i in g:
	b[i] = 0

a = "101 & 011 & 111 & 100 & 001 & 001 & 100 & 001 & 101 & 110 & 010 & 101 & 101 & 110 & 010 & 101"
a = a.split(" & ")

for i in a:
	b[i] += 1

for i in g:
	print i, b[i]
