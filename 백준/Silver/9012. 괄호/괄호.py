#https://www.acmicpc.net/problem/9012


import sys

#스택 활용하기

T = int(sys.stdin.readline())

for _ in range(T):
    vps = sys.stdin.readline()
    stack = []

    for i in vps:
        if i == "(":
            stack.append(i)
        elif i == ")":
            #스택에 괄호가 있다면
            if stack:
                stack.pop()
            else: #스택에 괄호가 없을 경우 올바른 괄호 X
                print("NO")
                break
    else: #break없이 끝났을 경우
        if not stack:
            print("YES")
        else: #break 안 걸렸어도 괄호가 들어가있다면 NO
            print("NO")


