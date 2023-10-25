from collections import deque
def solution(cards1, cards2, goal):
    answer = ''
    
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)
    
    # 먼저 끝난 list
    end = ''
    
    while goal:
        
        if len(cards1) == 0 or len(cards2) == 0:
            break
            
        # goal 문자 순서대로 있는 지 확인
        check1 = cards1.popleft()
        check2 = cards2.popleft()
        g = goal.popleft()
        
        if g == check1:
            cards2.appendleft(check2)
        elif g == check2:
            cards1.appendleft(check1)
    if len(goal) == 0:
        answer = "Yes"
    else:
        if len(cards1) == 0:
            if cards2 == goal:
                answer = "Yes"
            else:
                answer = "No"
        elif len(cards2) == 0:
            if cards1 == goal:
                answer = "Yes"
            else:
                answer = "No"
            
            
    
# 반례입니다.
# 입력값 〉 ["list", "length", "important"], ["are", "very"], ["are", "very"]
# 기댓값 〉 "Yes"
        
    return answer