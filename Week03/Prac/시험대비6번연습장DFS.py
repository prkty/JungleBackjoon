import sys

input =sys.stdin.readline

def dfs(graph, startnode):
    stack, visit = [], []
    stack.append(startnode)
    
    while stack:
        node = stack.pop()
        
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])
    return visit

computer = int(input())
M = int(input())

graph = {i: [] for i in range(1, computer + 1)}

for _ in range(M):
    u,v=map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
infect_computer = dfs(graph,1)
print(len(infect_computer)-1)