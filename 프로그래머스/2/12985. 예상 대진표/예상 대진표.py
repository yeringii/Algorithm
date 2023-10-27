def solution(n,a,b):
    cnt=0
    while True:
        # 같은 번호를 얻기 전까지
        a= (a//2)+(a%2) # 다음 번호
        b= (b//2)+(b%2) # 다음 번호 
        cnt+=1
        if a==b:
            break
    return cnt