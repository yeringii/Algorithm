import sys
from itertools import combinations
n, m = map(int, sys.stdin.readline().split()) # 회원의 수, 치킨 종류의 수

fav = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

result = 0 # 최대 만족도 합
for a, b, c  in combinations(range(m), 3):
    temp = 0
    for i in range(n):
        temp += max(fav[i][a], fav[i][b], fav[i][c])
    result = max(result, temp)
    
print(result)
