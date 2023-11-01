def solution(numbers):
    nums = [num  for num in range(0, 10)]
    answer = sum(set(nums) - set(numbers))
    return answer