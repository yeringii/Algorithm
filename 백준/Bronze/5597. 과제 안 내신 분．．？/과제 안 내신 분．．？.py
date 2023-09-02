import sys
#1-30 출석번호
all_nums = [ i for i in range(1,31)]
nums = []
for _ in range(28):
    nums.append(int(sys.stdin.readline()))

nums.sort()
# 미제출 출석 번호
result = list(set(all_nums) - set(nums))

# 미제출 출석 번호 작은 값, 그 다음 출석번호 출력
print(min(result))
print(max(result))
