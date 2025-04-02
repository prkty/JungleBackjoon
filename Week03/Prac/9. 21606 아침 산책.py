# 이 문제는 이해부터 어렵다. 주요 요지는 중간에 있는 노드가 실내면 안된다는 것이다.
# 그러므로  실내/실외 노드끼리 직접 연결된 경우의 수를 찾고 이에따라 수식은
# 노드 k개 가능 경로수 = k*(k-1)/2 으로 유도할 수 있다.
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

# 해당 문제의 전체적인 흐름은 이해됐다. 만약에 시간이 남으면 완벽히 이해해보겠다.
# GPT가 틀려서 claude 모델을 사용하여 답을 다시 구했다.
# 추후에 코드를 이해해 보겠다.

# 코드 설명
# 입력 처리:
# N: 정점의 개수
# A: 각 정점의 실내/실외 정보 (0: 실외, 1: 실내)
# 그래프 구성: 양방향 간선으로 그래프 만들기


# 실내-실내 직접 연결 계산:
# 모든 실내 정점에 대해, 인접한 다른 실내 정점과의 연결을 계산합니다.
# 이 경우 산책은 한 실내 정점에서 다른 실내 정점으로 바로 이동하는 것입니다.


# 실외를 통한 연결 계산:
# DFS를 사용하여 각 실외 컴포넌트(연결된 실외 정점들의 집합)를 탐색합니다.
# 각 실외 컴포넌트와 연결된 실내 정점의 수를 세고, 이를 이용해 가능한 경로 수를 계산합니다.
# 실내 정점 n개가 하나의 실외 컴포넌트와 연결되어 있다면, 그 사이의 가능한 경로 수는 n*(n-1)입니다.


# 최종 결과:
# 두 케이스에서 계산한 경로 수를 합하여 출력합니다.
# 산책은 방향이 있는 경로이므로 (A->B와A B->A는 다른 경로), 경로 수를 2로 나눌 필요가 없습니다.