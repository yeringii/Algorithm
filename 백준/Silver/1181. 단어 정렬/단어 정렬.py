'''
단어 정렬

알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

1. 길이가 짧은 것부터
2. 길이가 같으면 사전 순으로
'''

import sys

N = int(input())

word_list = set()

for _ in range(N):

    word = sys.stdin.readline().rstrip() #rstrip() 은 입력 후 엔터가 사용되므로

    word_list.add(word)

word_list = list(word_list)
word_list.sort()
#길이순으로 정렬
word_list.sort(key=lambda x : len(x))

#출력
for i in range(len(word_list)):
    print(word_list[i])