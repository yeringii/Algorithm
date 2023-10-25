def solution(k, score):
    answer = []
    check = []
    for i in range(len(score)):
        if i < k:
            check.append(score[i])
            check.sort(reverse=True)
            answer.append(min(check))
        else:
            check.append(score[i])
            check.sort(reverse=True)
            # 맨 뒤에 있는 값 삭제
            check.pop()
            answer.append(min(check))
    return answer