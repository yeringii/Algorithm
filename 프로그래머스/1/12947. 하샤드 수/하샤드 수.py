def solution(x):
    answer = str(x)
    sum = 0
    for i in answer:
        sum += int(i)
    if x%sum ==0:
        return True
    return False