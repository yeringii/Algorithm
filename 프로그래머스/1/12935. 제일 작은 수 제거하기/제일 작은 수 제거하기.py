def solution(arr):
    wrong = [-1]
    if (len(arr) > 1):
        
        minnum = min(arr)
        arr.remove(minnum)
    else:
        return wrong
        
    return arr