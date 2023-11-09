import sys

n = int(sys.stdin.readline())
l = []

for _ in range(n):
	l.append(int(sys.stdin.readline()))
count = 0
max = 0
for x in reversed(l):
	if max < x:
		max = x
		count += 1
print(count)