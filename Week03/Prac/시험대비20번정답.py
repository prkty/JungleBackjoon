import sys
input = sys.stdin.readline
from collections import deque


N, M = map(int, input().split())

indegree = [0] * (N + 1)

graph = [[] for i in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B) # 정점 A에서 B로 이동 가능
    # 진입 차수를 1 증가(A가 부모고 B가 자손이므로)
    indegree[B] += 1

def topology_sort():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용(디그리가 0인 정점 저장)

    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()  # 디그리 0인 정점 빼서 결과에 넣음
        result.append(now)
        
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    # 위상 정렬을 수행한 결과 출력
    for i in result:
        print(i, end=' ')

topology_sort()