import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 늘리기

def dfs(node, graph, A, visited):
    """
    DFS를 통해 하나의 실외 컴포넌트와 연결된 실내 노드의 수를 세는 함수
    node: 현재 탐색 중인 노드 (실외 노드)
    graph: 그래프 정보
    A: 각 노드의 실내/실외 정보
    visited: 방문 여부 배열
    return: 해당 실외 컴포넌트와 연결된 실내 노드의 수
    """
    visited[node] = True
    indoor_count = 0
    
    for neighbor in graph[node]:
        if A[neighbor-1] == '1':  # 인접한 노드가 실내이면 카운트
            indoor_count += 1
        elif A[neighbor-1] == '0' and not visited[neighbor]:  # 인접한 노드가 실외이고 아직 방문하지 않았으면 탐색 진행
            indoor_count += dfs(neighbor, graph, A, visited)
    
    return indoor_count

# 입력 처리
N = int(sys.stdin.readline().strip())  # 정점의 개수
A = sys.stdin.readline().strip()  # 정점의 실내/실외 정보 (0: 실외, 1: 실내)

# 그래프 구성
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

# 산책 경로 계산
answer = 0

# Case 1: 실내-실내 직접 연결
for i in range(1, N+1):
    if A[i-1] == '1':  # 실내 노드
        for neighbor in graph[i]:
            if A[neighbor-1] == '1':  # 인접한 실내 노드
                answer += 1

# Case 2: 실외 컴포넌트를 통한 실내-실내 연결
visited = [False] * (N+1)
for i in range(1, N+1):
    if A[i-1] == '0' and not visited[i]:  # 아직 방문하지 않은 실외 노드
        indoor_nodes = dfs(i, graph, A, visited)
        # 해당 실외 컴포넌트를 통해 연결될 수 있는 실내 노드 쌍의 개수 계산
        answer += indoor_nodes * (indoor_nodes - 1)

# 산책 경로는 시작점과 도착점이 다른 경로이므로 양방향으로 각각 세어야 함
print(answer)