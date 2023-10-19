def solution(food):
    answer = ''
    
    for i in range(1, len(food)):
        temp = ''
        re  = food[i] // 2
        temp = str(i) * re
        answer += temp
    # 물 추가
    answer += '0'
    # 상대편 음식
    filter_answer = answer.replace("0", "")
    reverse_answer = filter_answer[::-1]
    # 상대편 음식 추가 
    answer += reverse_answer
    
    return answer