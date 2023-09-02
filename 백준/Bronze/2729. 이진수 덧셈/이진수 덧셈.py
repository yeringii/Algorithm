import sys

t = int(sys.stdin.readline())

for _ in range(t):
    a, b = map(str, sys.stdin.readline().split())
    result = int(a, 2) + int(b, 2) #이진수 덧셈
    print(bin(result)[2:]) #이진수로 표현