def solution(s):
    answer = ""
    st = s.split(" ")
    st = list(map(int,st))
    maxval = max(st)
    minval = min(st)
    answer = "" +str(minval) +" "+ str(maxval) + ""
    return answer