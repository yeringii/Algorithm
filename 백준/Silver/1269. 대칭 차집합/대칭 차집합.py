#https://www.acmicpc.net/problem/1269


#두 집합 A와 B가 있을 때, (A-B)와 (B-A)의 합집합을 A와 B의 대칭 차집합이라고 한다.

N, M = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

#A-B + B-A
answer = len(A-B) + len(B-A)

print(answer)