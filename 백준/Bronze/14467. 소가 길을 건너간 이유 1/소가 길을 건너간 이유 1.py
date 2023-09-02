import sys

n = int(sys.stdin.readline())

#관찰 기록
record = dict()
count = 0
for _ in range(n):
    #소 번호, 위치
    cow, location = map(int, sys.stdin.readline().split())
    if cow in record: #등록되었다면 위치 변경 확인
        if record[cow] != location:
            count += 1
    record[cow] = location

print(count)

