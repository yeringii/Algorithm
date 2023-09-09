import sys, heapq

n = int(sys.stdin.readline())
nums = []
for _ in range(n):
    num = int(sys.stdin.readline())

    if num != 0:
        heapq.heappush(nums,num)
    else:
        if len(nums) == 0:
            print(0)
        else:
            print(heapq.heappop(nums))
