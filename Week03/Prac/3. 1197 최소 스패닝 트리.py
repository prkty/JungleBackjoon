# 최소 스패닝 트리를 풀기 위해서는 크루스칼과 프림 알고리즘이 있다.
# 그러나 크루스칼은 유니온 파인드라는 이론을 알아야하기 때문에 프림 알고리즘으로 구현해봤다.
# 프림 알고리즘은 임의의 노드에서 시작해서 다음 노드중 가장 적은 비용의 간선을 찾으면서 확장합니다.

# 다음은 V 정점에 해당되는 E개의 간선 정보를 받아 합해서 최소 신장 트리의 가중치 합을 출력하는 원리의 코드이다.
import sys
import heapq

def prim(V, edges):    # 입력된 정점 개수 V와 간선 값을 받는다.
    # 그래프를 인접 리스트 형태로 저장 (1번 노드부터 V번 노드까지 빈 리스트 초기화)
    graph = {i: [] for i in range(1, V + 1)}   
    
    # 간선 정보를 인접 리스트에 추가 u와 v는 정점 (양방향 그래프이므로)
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
            
             # 현재 노드(u)와 연결된 간선들을 확인하여 우선순위 큐에 추가
            for v, w in graph[u]:
                if not visited[v]:    # 아직 방문하지 않은 노드라면
                    heapq.heappush(priority_queue, (w, v))   # 우선순위 큐에 추가
    
    return mst_weight   # 최종 최소 신장 트리 합 리턴

# 입력 받기
V, E = map(int, sys.stdin.readline().split())
edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(E)] # 간선의 개수 E만큼 값을 받는다.(2차원 배열)

# 결과 출력
print(prim(V, edges))


# 여러 최소신장 트리 구하는 코드중에 위의 코드가 간결하고 이해하기 용이한 것 같다.
# 해당 코드들을 잘 외워보겠다.