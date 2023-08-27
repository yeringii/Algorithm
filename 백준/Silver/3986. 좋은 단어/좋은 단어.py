#https://www.acmicpc.net/problem/3986

'''
평석이는 단어 위로 아치형 곡선을 그어 같은 글자끼리(A는 A끼리, B는 B끼리) 쌍을 짓기로 하였다.
만약 선끼리 교차하지 않으면서 각 글자를 정확히 한 개의 다른 위치에 있는 같은 글자와 짝 지을수 있다면, 그 단어는 '좋은 단어'이다.

생각이 모자라서 참고함
'''

import sys

n = int(sys.stdin.readline())

cnt = 0

for _ in range(n):
    word = sys.stdin.readline().rstrip()
    stack = []
    for i in range(len(word)):
        #스택에 있는 맨 끝값과 비교해서 맞으면 바로 삭제
        if stack and word[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(word[i])
    #좋은 단어라면 stack이 비워졌을 것
    if len(stack) == 0:
        cnt += 1
print(cnt)



