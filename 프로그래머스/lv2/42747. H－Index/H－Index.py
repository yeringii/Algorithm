'''
테스트 9번 틀릴 경우
[10, 10, 10, 10, 10] 5
h-index 쉽게 푸는 방법 참고
https://postechlibrary.tistory.com/489
'''

def solution(citations):
    answer = 0
    citations = sorted(citations, reverse=True)
    
    for idx in range(len(citations)):
        if idx+1 <= citations[idx]:
            answer = idx+1
            continue
        else:
            answer = idx
            break
    
    return answer