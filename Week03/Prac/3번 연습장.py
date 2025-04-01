import sys
import heapq

def prim(V, edges):
    graph= {i: [] for i in range(1, V+1)}
    
    
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
        
    mst_weight = 0
    visted = [False] * (1+V)
    priority_queue = [(0, 1)]
    
    while priority_queue:
        weight, u = heapq.heappop(priority_queue)
        if not visted[u]:
            visted[u] = True
            mst_weight += weight
            
            for v, w in graph[u]:
                if not visted[v]:
                    heapq.heappush(priority_queue,(w,v))
                              
    return mst_weight



V, E = map(int,sys.stdin.readline().split())
edges = [tuple(map(int, sys.stdin.readline().split())) for _ in range(E)]

print(prim(V, edges))