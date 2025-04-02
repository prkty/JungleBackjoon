import sys
import heapq

input = sys. stdin.readline
INF = int(1e9)

N = int(input())
M = int(input())

graph = [[]for _ in range(1 + N)]
distance = [INF] * (N + 1)

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))
    
start, end = map(int, input().split())

def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0
    
    while pq:
        dist, now = heapq.heappop(pq)
        
        if distance[now] < dist:
            continue
        
        for next_node, cost in graph[now]:
            new_dist = dist + cost
            
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heapq.heappush(pq, (new_dist, next_node))
                
dijkstra(start)

print(distance[end])