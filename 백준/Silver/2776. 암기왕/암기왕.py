import sys

t = int(sys.stdin.readline())
#수첩 2
note_two = []
for _ in range(t):
    n = int(sys.stdin.readline())
    # 수첩 1
    note_one = set(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    # 수첩 2
    note_two = list(map(int, sys.stdin.readline().split()))
    note_two_set = set(note_two)
    # 수첩 1 & 수첩 2 교집합
    correct = note_one.intersection(note_two_set)
    #
    for num in note_two:
        if num in correct:
            print(1)
        else:
            print(0)