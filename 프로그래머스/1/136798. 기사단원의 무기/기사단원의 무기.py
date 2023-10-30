import math

def count_divisors_up_to_n(n):
    # 에라토스테네스의 체를 사용하여 각 수의 약수 개수를 계산
    divisors = [0] * (n + 1)
    
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            divisors[j] += 1

    return divisors


def solution(number, limit, power):
    answer = 0
    divisor_counts = count_divisors_up_to_n(number)
    # 필요한 철의 무게 계산
    for cnt in divisor_counts:
        if cnt > limit:
            answer += power
        else:
            answer += cnt
    return answer