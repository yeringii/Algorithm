import sys
n = int(sys.stdin.readline())
#각 선수의 성 저장할 곳
named = {}
for _ in range(n):
    first_name = sys.stdin.readline().rstrip()
    if first_name[0] not in named:
        named[first_name[0]] = 1
    else:
        named[first_name[0]] += 1
#사전순으로 정렬
named = sorted(named.items())
#정답
result = ''

for k,v in named:
    if v >= 5:
        result += k
    else:
        continue
#정답 출력
if result:
    print(result)
else:
    print("PREDAJA")