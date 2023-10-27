# 접근법 거의 다 왔는데 참고해서 풂

def solution(n):
    ans = 0
    
    while n > 0 :
        ans += n % 2
        n = n//2

    return ans