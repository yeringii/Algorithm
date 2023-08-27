#acmicpc.net/problem/1966

'''
현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.

다시 풀어보기 너무 우선순위큐만 구해서 하려고 해서 못풀음

참고해서 품 ->https://moonlight-spot.tistory.com/entry/%EB%B0%B1%EC%A4%80-1966-%ED%94%84%EB%A6%B0%ED%84%B0-%ED%81%90-in-%ED%8C%8C%EC%9D%B4%EC%8D%AC
'''

'''
중요도 큐의 맨 앞의 원소가 가장 큰 값이면 출력하고(popleft()), 아니라면 큐의 뒤로 보낸다.
'''


import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    #n: 문서 개수, target: 몇번째로 인쇄됐는지 궁금한 문서
    n, target_num = map(int, sys.stdin.readline().split())
    q= deque(list(map(int, sys.stdin.readline().split())))
    idx = deque(list(range(n)))
    #몇 번째로 출력되는지
    cnt = 0
    
    #중요도가 가장 높은 원소가 앞에오면 출력, 아니면 뒤로 append
    while q:
        if q[0] == max(q):
            cnt += 1
            q.popleft()
            pop_idx = idx.popleft()
            #만약 찾고자 하는 문서가 출력됐으면
            if pop_idx == target_num:
                print(cnt)
        #중요도 높은 값이 아니라면 큐 뒤로 보냄
        else:
            q.append(q.popleft())
            idx.append(idx.popleft())
            
        
    
    
    
    
    # #몇 번째에 있는지 궁금한 문서의 중요도
    # target = -importance[target_num]
    
    # #최대 우선순위큐
    # que = PriorityQueue()
    
    # #(중요도, 문서 idx)
    # for i in range(n):
    #     que.put((-importance[i], i))
    
    # #출력
    # for i in range(que.qsize()):
    #     # print(que.get())
    #     #item (중요도, 문서 idx)
    #     it, idx = que.get()
    #     if -it == target_num:
    #         print(i)
    