# 감이 안잡혀서 GPT의 도움을 받아 이해하고 코드를 분석했다.
# 시작 노드를 설정하고, 거리를 0으로 초기화 합니다.
# 우선 순위 큐를 사용하여 가장 짧은 거리를 가진 노드를 선택.
# 선택된 노드의 인접 노드들의 최단 거리를 갱신합니다.
# 모든 노드를 방문할 때까지 위 과정을 반복합니다.

import sys
import heapq

input = sys.stdin.readline  # 빠른 입력
INF = int(1e9)  # 무한대 값 (10억)

# 1. 입력 받기
N = int(input())  # 도시 (노드) 개수
M = int(input())  # 버스 (간선) 개수

# 2. 그래프 및 거리 테이블 초기화
graph = [[] for _ in range(N + 1)]  # 인접 리스트 (1-based index)
distance = [INF] * (N + 1)  # 최단 거리 테이블 (INF로 초기화)

# 3. 그래프 정보 입력 받기
for _ in range(M):
    u, v, w = map(int, input().split())  # u에서 v로 가는 비용 w
    graph[u].append((v, w))  # 방향 그래프 정점 u의 (정점v까지의, 가중치w)

# 4. 출발점과 도착점 입력 받기
start, end = map(int, input().split())

# 5. 다익스트라 알고리즘 (우선순위 큐 사용)
def dijkstra(start):
    pq = []  # 우선순위 큐 (Min-Heap)
    heapq.heappush(pq, (0, start))  # (비용, 시작점) 추가
    distance[start] = 0  # 시작점 거리는 0으로 설정

    while pq:  # 큐가 빌 때까지 반복
        dist, now = heapq.heappop(pq)  # 현재 거리와 노드 번호 가져오기

        if distance[now] < dist:  # 이미 처리된 노드라면 무시
            continue

        # 현재 노드와 연결된 다른 노드 확인
        for next_node, cost in graph[now]:
            new_dist = dist + cost  # 현재까지 거리 + 이동 비용 = 새 거리

            if new_dist < distance[next_node]:  # 더 짧은 경로 발견 시 갱신
                distance[next_node] = new_dist
                heapq.heappush(pq, (new_dist, next_node))  # 우선순위 큐에 추가

# 6. 다익스트라 실행
dijkstra(start)

# 7. 도착점까지의 최소 비용 출력
print(distance[end])

# 거의다 이해는 됐는데, 코드 짜라고 하면 못짤 것 같아서 많은 반복 해야겠다...