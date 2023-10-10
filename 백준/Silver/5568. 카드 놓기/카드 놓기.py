from itertools import permutations
import sys
n = int(sys.stdin.readline())  # 카드의 개수
k = int(sys.stdin.readline())  # 선택할 숫자의 개수
cards = [sys.stdin.readline().rstrip() for _ in range(n)]  # 카드에 적힌 숫자 리스트

# 순열을 이용하여 가능한 모든 조합을 생성
combos = set()
for perm in permutations(cards, k):
    combos.add(''.join(perm))

# 중복을 제거한 조합의 개수 출력
print(len(combos))