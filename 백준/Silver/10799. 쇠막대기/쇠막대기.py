s = input()  # 괄호 문자열 입력
stack = []   # 스택 초기화
count = 0    # 잘린 쇠막대기 조각 수

for i in range(len(s)):
    if s[i] == '(':  # 여는 괄호일 때
        stack.append('(')
    else:  # 닫는 괄호일 때
        if s[i-1] == '(':  # 직전이 여는 괄호인 경우
            stack.pop()    # 스택에서 여는 괄호를 빼고
            count += len(stack)  # 현재 스택의 길이를 조각 수에 추가
        else:  # 직전이 닫는 괄호인 경우
            stack.pop()    # 스택에서 하나 빼고
            count += 1  # 조각 수에 1 추가

print(count)
