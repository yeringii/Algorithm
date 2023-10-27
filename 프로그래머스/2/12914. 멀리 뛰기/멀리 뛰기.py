# gpt 도움 받아서 해결 dp로 하는 거 연습 필요
def count_ways(n):
    if n <= 1:
        return 1
    elif n == 2:
        return 2

    # 1칸 또는 2칸 뛰는 경우를 저장할 배열
    ways = [0] * (n + 1)

    ways[0] = 1  # 출발점
    ways[1] = 1  # 1칸 이동
    ways[2] = 2  # 2칸 이동

    for i in range(3, n + 1):
        ways[i] = ways[i - 1] + ways[i - 2]

    return ways[n]


def solution(n):
    answer = count_ways(n) % 1234567
    
    return answer