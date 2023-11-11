#https://www.acmicpc.net/problem/2161

'''
카드 한 장 남을때까지 반복
1. 제일 위에 있는 카드 바닥에 버림
2. 그 다음 위에 있는 카드 제일 아래로 옮김

한 장 남을때까지 계속

'''

from collections import deque
import sys


N = int(sys.stdin.readline())

cards = deque([n for n in range(1,N+1)])

while cards:
    if len(cards) == 1:
        print(cards.popleft())
        break
    #제일 위에 있는 카드 버림
    c = cards.popleft()
    print(c, end=' ')
    #그 다음 위에 있는 카드 맨 끝으로
    next_c = cards.popleft()
    cards.append(next_c)
