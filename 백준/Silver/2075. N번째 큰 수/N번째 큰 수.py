import sys, heapq

n = int(sys.stdin.readline())

heap = []

#처음에는 N개의 수를 heapq에 넣은 뒤 다음 수 부터는 heapq에서 N번째 큰 수와 비교,
#크면 heapq에서 N번째 수 대신 넣고 작으면 넣지 않음

for i in range(n):
    nums = list(map(int, sys.stdin.readline().split()))
    if i == 0:
        for num in nums:
            heapq.heappush(heap,num)
    else:
        for num in nums:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap,num)
print(heapq.heappop(heap))
