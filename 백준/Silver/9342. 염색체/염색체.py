# https://www.acmicpc.net/problem/9342


'''
문자열은 {A, B, C, D, E, F} 중 0개 또는 1개로 시작해야 한다.
그 다음에는 A가 하나 또는 그 이상 있어야 한다.
그 다음에는 F가 하나 또는 그 이상 있어야 한다.
그 다음에는 C가 하나 또는 그 이상 있어야 한다.
그 다음에는 {A, B, C, D, E, F} 중 0개 또는 1개가 있으며, 더 이상의 문자는 없어야 한다.

정규표현식 문제
^ 해당 패턴으로 시작
? 해당 패턴을 0번또는 1번
$ 해당 패턴으로 끝
+ 해당 패턴이 하나 이상
'''

import re

pattern = re.compile('^[A-F]?A+F+C+[A-F]?$')
for _ in range(int(input())):
    if pattern.match(input()) == None:
        print('Good')
    else:
        print('Infected!')