# https://www.acmicpc.net/problem/20291


import sys

n = int(sys.stdin.readline())

extensions = {}

for _ in range(n):
    file, ex = map(str, sys.stdin.readline().rstrip().split("."))
    #파일 이름, 확장자
    if ex not in extensions:
        extensions[ex] = 1
    else:
        extensions[ex] += 1

result = sorted(extensions.items(), key=lambda x: x[0])

for ex, cnt in result:
    print(ex, cnt)