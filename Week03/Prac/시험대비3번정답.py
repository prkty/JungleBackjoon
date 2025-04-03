import sys
import heapq

def prim(V, edges):    
    graph = {i: [] for i in range(1, V + 1)}   
    
    for u, v, w in edges:
        graph[u].append((v, w))  # u에서 v로 가는 간선 w
        graph[v].append((u, w))  # v에서 u로 가는 간선 w
    
    mst_weight = 0   # 최소 신장 트리의 가중치 합을 저장할 변수
    visited = [False] * (V + 1)   # 방문 여부 체크 리스트 (1-based index 사용, 1번부터 인덱스 시작)
    priority_queue = [(0, 1)]  # (가중치, 시작 노드) 형태의 우선순위 큐 (초기값: 0번 가중치로 1번 노드 시작)
    
    while priority_queue:
        weight, u = heapq.heappop(priority_queue)  # 가중치가 가장 작은 간선 선택
        if not visited[u]:   # 해당 노드가 방문되지 않았다면
            visited[u] = True  # 방문 완료 처리
            mst_weight += weight   # 최소 신장 트리 합에 추가

            for v, w in graph[u]:
                if not visited[v]:    # 아직 방문하지 않은 노드라면
                    heapq.heappush(priority_queue, (w, v))   # 우선순위 큐에 추가
    
    return mst_weight   # 최종 최소 신장 트리 합 리턴

V, E = map(int, sys.stdin.readline().split())
edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(E)] # 간선의 개수 E만큼 값을 받는다.(2차원 배열)

print(prim(V, edges))
