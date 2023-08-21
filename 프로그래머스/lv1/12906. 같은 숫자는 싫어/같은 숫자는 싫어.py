def solution(arr):
    answer = []
    answer.append(arr[0])
    for num in arr:
        # 마지막에 들어있는 값과 비교해서 삽입
        if answer[-1] == num:
            continue
        else:
            answer.append(num)
    return answer