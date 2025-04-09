import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
INF = int(1e9)

graph=[[INF] * (1 + N) for _ in range(1 + N)]

for i in range(1, N + 1):
    graph[i][i] = 0
    
    
for _ in range(M):
    a,b,c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)
    
    
for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            graph[i][j] = min(graph[i][j], graph[k][i] + graph[k][j])
            
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()