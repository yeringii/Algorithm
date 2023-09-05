'''
듣보잡
'''


import sys

N,M = map(int,sys.stdin.readline().split())

n_list = []
m_list = []

#듣도 못한 사람
for _ in range(N):
    name = sys.stdin.readline().rstrip()
    n_list.append(name)

#보도 못한 사람
for _ in range(M):
    name = sys.stdin.readline().rstrip()
    m_list.append(name)
#듣도 보도 못한 사람 -> 리스트 교집합 이용
intersect = list(set(n_list) & set(m_list))
#사전 순
intersect.sort()
#출력
print(len(intersect))
for name in intersect:
    print(name)