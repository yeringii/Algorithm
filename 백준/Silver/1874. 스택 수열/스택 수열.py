import sys
n = int(sys.stdin.readline())


stack = []
op = [] #push, pop 모음
target = 1 #1-n까지의 숫자값
check = True #스택 수열 가능 확인 체커

for _ in range(n):
    seq = int(sys.stdin.readline()) #임의의 수열
    #seq 이하 스택에 추가
    while target <= seq:
        stack.append(target)
        op.append('+')
        target += 1 #target 증가
    #입력받은 seq와 스택 맨 위 숫자와 동일하다면 제거
    if seq == stack[-1]:
        stack.pop()
        op.append('-')
    #스택 맨 위 숫자와 동일하지 않는다면 수열을 만들 수 없음
    else:
        check = False
        break

if check == False:
    print('NO')
else:
    for i in op:
        print(i)



