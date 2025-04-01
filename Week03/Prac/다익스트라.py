import sys
import heapq

n, m = map(int, sys.stdin.readline().split())

start = int(sys.stdin.readline())
INF = 100000000000

distance = [INF] * (n+1)
graph = [[] for _ in range(n+1)]
for  _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for next in graph[node]:
            cost = distance[node] + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))

for i in range(1, len(distance)):
    if distance[i] == INF:
        print('도달할 수 없음')
    else:
        print(distance[i])
