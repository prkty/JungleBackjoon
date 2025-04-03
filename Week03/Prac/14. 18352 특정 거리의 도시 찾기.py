# 도시와 도로의 개수가 주어지면 최단 거리 기준 K인 도시가 무엇인지 뽑는 문제이다.
# 만약에 도달할 수 있는 도시가 없다면 -1을 출력한다.
# BFS로 한 단계식 탐색하며 찾다가 K 거리에 도달하면 결과를 저장한다.
# 그래프 리스트로 도시들을 관리하고 거리 리스트로 -1로 초기화해 거리를 저장한다.
# 큐를 통해 도시를 탐색하고 거리를 갱신한다.
import sys
from collections import deque

input = sys.stdin.readline

# 도시 개수(N), 도로 개수(M), 거리 정보(K), 출발 도시(X) 입력
N, M, K, X = map(int, input().split())

# 그래프 초기화 (인접 리스트 방식)
graph = {i: [] for i in range(1, N+1)}

# 간선 정보 입력받기
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)  # 단방향 그래프이므로 a -> b만 저장 받음

distance = [-1] * (N + 1)  # 모든 도시까지의 최단 거리 리스트 (초기값 -1 그래야 갱신가능)
distance[X] = 0  # 출발 도시의 거리는 0, X가 출발 도시이므로
queue = deque([X])  # BFS 구현 (큐 사용) 시작점 큐에 추가

while queue:  # 큐가 빌 때 까지 수행
    current = queue.popleft()  # 현재 탐색 중인 도시

    for next_city in graph[current]:   # 연결된 도시들 확인
        # current(0등)에서 이동할 수 있는 도시(next_city)를 찾음
        if distance[next_city] == -1:  # 방문하지 않은 도시라면
            distance[next_city] = distance[current] + 1  # 거리 갱신
            # 현재 도시에서 다음 도시까지 거리가 1이므로 +1을 해준다.
            queue.append(next_city)  # 큐에 추가

# 결과 출력 (N개의 도시에서 거리 K인 도시 찾기)
result = [i for i in range(1, N+1) if distance[i] == K]

# 결과가 없으면 -1 출력, 있으면 정렬 후 출력
if result:
    for city in sorted(result):  # 도시를 오름차순으로 출력
        print(city)
else:
    print(-1)   # 결과 없다면 -1 출력
    
# 앞 전의 미로 탐색 문제랑 살짝 다르다. 리스트를 쓰고 최단 거리를 구하는 문제이다.
# 이게 문제마다 코드가 달라지니 BFS가 DFS보다 더 어려운 것 같다.
# 중간의 while하고 for문이 이 문제에 핵심으로 잘 아는 것이 좋을 것 같다.
# 코드 이해는 완료됐지만 외우지는 못했다.
