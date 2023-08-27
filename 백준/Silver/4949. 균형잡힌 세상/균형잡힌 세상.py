#https://www.acmicpc.net/problem/4949


'''
https://velog.io/@pmk4236/%EB%B0%B1%EC%A4%80-4949%EB%B2%88-%EA%B7%A0%ED%98%95%EC%9E%A1%ED%9E%8C-%EC%84%B8%EC%83%81-Python
'''
while True :
    a = input()
    stack = []

    if a == "." :
        break

    for i in range(len(a)):
        if a[i] == "(" or a[i] == "[":
            stack.append(a[i])
        elif a[i] == ")":
            if len(stack)!=0 and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(")")
                break
        elif a[i] == "]":
            if len(stack)!=0 and stack[-1] == "[":
                stack.pop()
            else:
                stack.append("]")
                break

    if len(stack)==0:
        print("yes")
    else:
        print("no")
