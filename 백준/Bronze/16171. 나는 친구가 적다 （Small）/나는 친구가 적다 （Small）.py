import sys

s = list(sys.stdin.readline().rstrip())
k = sys.stdin.readline().rstrip()

def find_alpha(str):
    result = []
    for s in str:
        if s.isalpha():
            result.append(s)
        else:
            continue
    return result
# 숫자 제거
new_s =''.join(find_alpha(s))

if k in new_s:
    print(1)
else:
    print(0)