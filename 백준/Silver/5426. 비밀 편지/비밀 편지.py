#https://www.acmicpc.net/problem/5426


'''
항상 제곱수
'''

import sys, math

T = int(sys.stdin.readline())


for _ in range(T):
    letter = sys.stdin.readline().rstrip()

    #제곱근
    sqrt =int(math.sqrt(len(letter)))

    #정사각형 행열로 만들기
    square = []
    # print(square)
    for i in range(0,len(letter),sqrt):
        tmp = ''
        for j in range(i,i+sqrt):
            tmp += letter[j]+' '
        square.append(tmp.split())
    # print(square)
    answer = ''


    for i in range(sqrt-1,-1,-1):
        for j in range(0, sqrt):
            answer += square[j][i]

    print(answer)


