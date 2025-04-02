import sys
import heapq

INF = float('inf')  # 무한대를 의미하는 값 설정

def dijkstra(V, E, start, edges):
    # 그래프를 인접 리스트로 표현 (1번 노드부터 시작)
    graph = {i: [] for i in range(1, V + 1)}
    for u, v, w in edges:
        graph[u].append((w, v))  # u라는 기준점에서 (가중치, 목적지 노드)형태로 값 저장
    
    # 최단 거리 테이블 초기화
    distance = [INF] * (V + 1)  # 모두 무한으로 초기화(그래야 비교해서 교체 가능, 0이면 안되므로)
    distance[start] = 0  # 시작 정점의 거리는 0
    
    # 우선순위 큐 (최소 힙) 사용
    pq = [(0, start)]  # (현재까지의 거리, 정점)
    
    while pq:
        cur_dist, cur_node = heapq.heappop(pq)  # 최단 거리 노드 선택
        if distance[cur_node] < cur_dist:
            continue  # 이미 처리된 노드라면 무시
        
        # 현재 노드의 인접 노드 확인
        for nxt_dist, nxt_node in graph[cur_node]:
            new_dist = cur_dist + nxt_dist
            
            if new_dist < distance[nxt_node]:  # 더 짧은 경로 발견 시 갱신
                distance[nxt_node] = new_dist
                heapq.heappush(pq, (new_dist, nxt_node))  # 우선순위 큐에 추가
    
    return distance

# 입력 받기
V, E = map(int, sys.stdin.readline().split())  # 정점 수 V, 간선 수 E
start = int(sys.stdin.readline())  # 시작 정점
edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(E)]  # 간선 정보 입력

# 다익스트라 실행 및 결과 출력
distances = dijkstra(V, E, start, edges)
for i in range(1, V + 1):
    print("INF" if distances[i] == INF else distances[i])
