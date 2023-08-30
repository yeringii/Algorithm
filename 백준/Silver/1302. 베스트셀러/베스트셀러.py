'''
베스트셀러 -> 도움 받아서 품

https://kau-algorithm.tistory.com/331

'''

import sys

N = int(sys.stdin.readline())

t_list = {}

for _ in range(N):
    title = sys.stdin.readline().rstrip()
    if title in t_list:
        t_list[title] += 1
    else:
        t_list[title] = 1

result = []

#가장 많이 팔린 책의 개수
best = max(t_list.values())

for i in t_list:
    if best == t_list[i]:
        result.append(i)

result.sort()

#가장 많이 팔린 개수가 똑같은 책 제목 -> 사전순으로 출력 (제일 앞에 존재)
print(result[0])


