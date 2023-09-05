import sys

s = sys.stdin.readline().rstrip()

#알파벳 대문자 획수
alpha = {'A':3,'B':2,'C':1,'D':2,'E':3,'F':3,'G':3,'H':3,'I':1,'J':1,
         'K':3,'L':1,'M':3,'N':3,'O':1,'P':2,'Q':2,'R':2,'S':1,'T':2,
         'U':1,'V':1,'W':2,'X':2,'Y':2,'Z':1}

result = 0

for i in range(0, len(s), 2):
    if (len(s)%2 == 1) and (i == len(s)-1):
        result += alpha[s[i]]
    else:
        if result >= 10:
            result %= 10
        add = alpha[s[i]] + alpha[s[i+1]]
        result += add
    if result >= 10:
        result %= 10
# 정답 판별
if result % 2 == 1:
    print("I'm a winner!")
else:
    print("You're the winner?")