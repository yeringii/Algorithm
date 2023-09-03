import sys
#선수들 번호 나올 때마다 포인트 +1
while True:
    n, m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0:
        break
    result = [0 for _ in range(10001)]
    for _ in range(n):
        player = list(sys.stdin.readline().split())
        for p in player:
            result[int(p)] += 1
    #1등 점수 제거
    result[result.index(max(result))] = 0
    m = max(result)
    #리스트 내 모든 최댓값 인덱스 저장
    answer = [ index for index, val in enumerate(result) if val == m]
    for ans in answer:
        print(ans, end=' ')
    print()