import sys
from collections import deque

#큐의 크기, 뽑아내려고 하는 수의 개수
n, m = map(int, sys.stdin.readline().split())
#뽑아내려는 수의 위치
index = list(map(int, sys.stdin.readline().split()))
deque = deque([i for i in range(1,n+1)])

#2,3번 연산 횟수 카운트
count = 0
for i in index: #뽑아내려는 수 위치 하나씩 순회
    while True: #뽑을 때까지 반복
        if i == deque[0]:
            deque.popleft()
            break
        else:
            if deque.index(i) < len(deque)/2: #뽑아내려는 수의 위치가 deque길이 반보다 작다면 왼쪽에서 찾아야함
                while deque[0] != i:
                    deque.append(deque.popleft())
                    count += 1 
            else: #뽑아내려는 수 위치가 deque길이 반보다 크다면 오른쪽에서 찾아야 함
                while deque[0] != i:
                    deque.appendleft(deque.pop())     
                    count += 1


print(count)

