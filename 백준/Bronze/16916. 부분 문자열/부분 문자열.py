'''
부분 문자열
'''

import sys

S = sys.stdin.readline().rstrip()
P = sys.stdin.readline().rstrip()

if S.find(P) == -1:
    print(0)
else:
    print(1)