from collections import Counter

n = int(input())

for _ in range(n):
    sentence = input()
    sentence = sentence.replace(" ", "") # 공백 제거
    # 가장 빈번하게 나타나는 문자
    count = Counter(sentence)
    # 상위 2개 항목
    result = sorted(count.items(), key=lambda pair: pair[1], reverse=True)
    # 만약 두 개의 값이 같다면, 빈번한 값이 여러개
    # 그렇지 않다면 빈번한 값이 유일함
    try:
        if result[0][1] == result[1][1]:
            print('?')
        else:
            print(result[0][0])
    except: # 문자열 종류가 하나인 경우 두번째 빈도수 구할 수 없음
        print(result[0][0])