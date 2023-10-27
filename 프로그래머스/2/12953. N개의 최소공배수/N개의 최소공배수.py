import math

# 두 수의 최소공배수를 계산하는 함수
def least_common_multiple(a, b):
    return a * b // math.gcd(a, b)

# 여러 개의 수의 최소공배수를 계산하는 함수
def multiple_least_common_multiple(numbers):
    result = 1
    for num in numbers:
        result = least_common_multiple(result, num)
    return result

def solution(arr):
    answer = multiple_least_common_multiple(arr)
    return answer