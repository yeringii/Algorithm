'''
대소문자 바꾸기
'''


import sys

word = sys.stdin.readline().rstrip()

result = ''

for i in range(len(word)):
    if word[i].isupper():
        result += word[i].lower()
    else:
        result += word[i].upper()

print(result)