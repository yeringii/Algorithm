import sys
n = int(sys.stdin.readline())

#'EW'가 되는 곳을 찾아 탐색
#E의 끝에 선물 배치 후 W가 나오면 선물을 무조건 가져감

map = sys.stdin.readline().rstrip()

result = map.count('EW')
print(result)