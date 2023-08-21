#deque 쓰기
from collections import deque
def solution(s):
    answer = True
    #큐 선언 -> deque(['(',')']) 이런식으로 들어감
    q = deque(s)
    #괄호 짝 확인 리스트
    check = []
    #큐가 빌 때까지
    while q:
        #bracket(괄호)
        bracket = q.popleft()
        #print("bracket : ", bracket)
        #리스트가 비어있다면
        if not check:
            check.append(bracket)
        else:
            #괄호 짝 맞는지 확인
            if bracket == ')':
                if check[-1] == '(':
                    del check[-1]
                #만약 짝이 안 맞는다면, 리스트에 넣기
                else:
                    check.append(bracket)
            else:
                check.append(bracket)
        #print("현재 리스트: ", check)
    #만약 리스트에 하나라도 남아있다면
    if check:
        answer = False
    
    #()()
    #(())()

    return answer