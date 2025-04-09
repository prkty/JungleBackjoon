import sys
input = sys.stdin.readline  # 입력을 빠르게 처리

n = int(input())   # 도시(노드) 개수

m = int(input())   # 버스(간선) 개수

INF = int(1e9)   # 무한대로 초기화 (10억 이상이면 충분)

# 2차원 거리 배열 초기화
# graph[i][j]는 i에서 j로 가는 최소 비용
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신으로 가는 비용은 0
for i in range(1, n + 1):
    graph[i][i] = 0

# 간선 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    # 여러 간선 중 더 짧은 값만 저장
    graph[a][b] = min(graph[a][b], c)

# 플로이드 워셜 알고리즘 수행(3중 for문)
for k in range(1, n + 1):           # 경유지
    for i in range(1, n + 1):       # 출발지
        for j in range(1, n + 1):   # 도착지
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 결과 출력
for i in range(1, n + 1):
    for j in range(1, n + 1):
        # 도달할 수 없으면 0 출력
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()
