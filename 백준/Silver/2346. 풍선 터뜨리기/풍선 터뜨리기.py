'''
참고 : https://velog.io/@hygge/Python-%EB%B0%B1%EC%A4%80-2346-%ED%92%8D%EC%84%A0-%ED%84%B0%EB%9C%A8%EB%A6%AC%EA%B8%B0-deque
'''
import sys
from collections import deque

n = int(sys.stdin.readline())

deq = deque(enumerate(map(int, sys.stdin.readline().split())))
result = []

while deq:
    idx, num = deq.popleft()
    result.append(idx+1)

    if num > 0:
        deq.rotate(-(num-1)) #이미 pop으로 왼쪽으로 회전되어 있는 상태, num-1만큼만 회전
    elif num < 0:
        deq.rotate(-num) #오른쪽으로 회전
        
print(' '.join(map(str, result)))
