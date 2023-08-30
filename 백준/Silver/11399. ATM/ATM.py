import sys

n = int(sys.stdin.readline())
time = list(sorted(map(int, sys.stdin.readline().split())))
answer = 0

for i in range(len(time)):
    for j in range(0,i+1):
        answer += time[j]
print(answer)