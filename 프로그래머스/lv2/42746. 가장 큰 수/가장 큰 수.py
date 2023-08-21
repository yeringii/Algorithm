# 문자열 비교연산 -> 문자열 첫 번째 인덱스를 아스키숫자로 바꿔서 비교, 같으면 그 다음 인덱스 비교
def solution(numbers):
    numbers = list(map(str, numbers))               #1. 정렬
    numbers.sort(key=lambda x: x*3, reverse=True)       #2. number는 1000이하의 숫자이므로 x3(반복)한 값으로 비교
    return str(int(''.join(numbers)))



'''
# 시간초과
from itertools import permutations
def solution(numbers):
    per_list = map(str,numbers) # str으로 변환
    per_list = list(permutations(per_list,len(numbers))) # 순열 조합
    temp = [''.join(per) for per in per_list] # join으로 조합 합치기
    answer = list(sorted(map(int, temp), reverse=True)) # int 변환 및 정렬

    return str(answer[0])
'''