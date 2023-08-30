'''
참고해서 풂
'''
import sys

tc = int(sys.stdin.readline())

for _ in range(tc):
    n = int(sys.stdin.readline())
    clothes = {}
    for _ in range(n):
        name, ctg = sys.stdin.readline().split()

        #종류별로 분류
        if ctg not in clothes.keys():
            clothes[ctg] = 1
        else:
            clothes[ctg] += 1
    ans = 1
    for i in clothes: #i:key
        ans *= clothes[i]+1 #해당 종류는 안 입는 경우 포함
    print(ans-1) #알몸 제외

