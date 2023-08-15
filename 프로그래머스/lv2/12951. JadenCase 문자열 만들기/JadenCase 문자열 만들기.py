def solution(s):
    answer = ''
    #capitalize() -> 문자열 첫글자만 대문자로 변환
    
    s = s.split(' ')
    for i in range(len(s)):
        s[i] = s[i].capitalize()
    print(s)
    answer = ' '.join(s)
    #print(s.capitalize())
        
            
    return answer