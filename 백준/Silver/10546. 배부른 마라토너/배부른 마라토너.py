import sys

n = int(sys.stdin.readline())
#참가한 사람
participant = {}
#완주한 사람
run = []

#참가자 이름
for _ in range(n):
    name = sys.stdin.readline().rstrip()
    if name not in participant:
        participant[name] = 1
    else:
        participant[name] += 1

#완주한 사람 n-1
for _ in range(n-1):
    run.append(sys.stdin.readline().rstrip())

#완주하지 못 한 사람 찾기
for name in run:
    if name in participant:
        participant[name] -= 1

print(max(participant,key=participant.get))