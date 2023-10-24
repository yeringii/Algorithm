def solution(name, yearning, photo):
    answer = []
    # 그리움 점수
    missing = {}
    for i in range(len(name)):
        if name[i] not in missing:
            missing[name[i]] = yearning[i]
    # 추억 점수 계산
    for i in range(len(photo)):
        score = 0
        for name in photo[i]:
            if name not in missing:
                continue
            else:
                score += missing[name]
        answer.append(score)
    return answer