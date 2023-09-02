'''
그룹 단어 체커

'''

import sys

N = int(sys.stdin.readline())

answer = 0
#aba 1(0,2) 2 (1,3)
for _ in range(N):
    word = sys.stdin.readline().rstrip()

    result = ''
    check = []
    # print(len(word))
    check.append(word[0])
    for idx in range(1,len(word)):
        if word[idx] not in check:
            check.append(word[idx])
        else:
            #연속되는지 확인(바로 전 단어와 비교)
            if check[idx-1] == word[idx]:
                check.append(word[idx])
            else:
                break
    #원래 문자열이랑 일치하는지 확인
    result = ''.join(check)
    # print(result)
    if result == word:
        answer += 1

print(answer)


