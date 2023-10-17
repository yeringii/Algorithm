# def solution(brown, yellow):
#     answer = []
#     plus = brown + yellow
#     # plus의 약수
#     nums = []
#     for n in range(1, plus+1):
#         if plus % n == 0:
#             nums.append(n)
#     # 가장 차이가 적게 나는 약수 갖고오기
#     if len(nums) % 2 == 0:
#         answer = nums[(len(nums)//2)-1 : (len(nums)//2)+1]
#         answer.sort(reverse=True)
#     else:
#         tmp = nums[len(nums)//2]
#         answer = [tmp, tmp]
    
#     return answer

def solution(brown, yellow):
    for col in range(1, int(yellow**0.5) + 1):
        if yellow % col == 0:
            row = yellow // col
            if 2 * row + 2 * col + 4 == brown:
                return [row + 2, col + 2]
