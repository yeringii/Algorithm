import sys

s = sys.stdin.readline().rstrip()

pikachu = ["pi", "ka", "chu"]

for p in pikachu:
    if p in s:
        s = s.replace(p,"*")

check = True
for i in s:
    if i != "*":
        check=False

if check:
    print("YES")
else:
    print("NO")