from collections import deque

n = int(input())
card = deque([ i for i in range(1,n+1)])

while True:
    if len(card) == 1:
        break
    card.popleft() #1.제일 위에 있는 카드를 바닥에 버림
    card.append(card.popleft()) #2. 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮김

print(card[0])