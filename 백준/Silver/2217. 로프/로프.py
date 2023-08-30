import sys

n = int(sys.stdin.readline())
w_list = []
for _ in range(n):
    w_list.append(int(sys.stdin.readline()))
w_list.sort(reverse=True)

answer = []
for i in range(n):
    answer.append(w_list[i] * (i+1))

print(max(answer))
