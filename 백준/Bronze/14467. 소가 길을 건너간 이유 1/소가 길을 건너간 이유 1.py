import sys

n = int(sys.stdin.readline())

#관찰 기록
record = dict()
count = 0
for _ in range(n):
    #소 번호, 위치
    cow, location = map(int, sys.stdin.readline().split())
    if cow in record: #아직 등록되지 않았다면 등록
        if record[cow] != location:
            count += 1
    record[cow] = location

print(count)

