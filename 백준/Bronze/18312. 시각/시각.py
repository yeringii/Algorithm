import sys

N, K = map(int, sys.stdin.readline().split())

cnt = 0

for h in range(N + 1):
    for m in range(60):
        for s in range(60):
            time_str = f"{h:02d}{m:02d}{s:02d}"
            if str(K) in time_str:
                cnt += 1

print(cnt)
