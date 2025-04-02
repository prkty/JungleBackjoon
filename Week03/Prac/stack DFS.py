import sys

input = sys.stdin.readline

def dfs(graph, start_node):   # dfs 구현부분
    stack, visit = [],[]   # 해당부분을 디렉토리로 안바꿔서 틀렸었다
    stack.append(start_node)   # 시작 노드를 스택에 먼저 입력한다.
    
    while stack:    # 스택에 사라질 때까지
        node = stack.pop()   # 스택에서 하나씩 pop한다.
        
        if node not in visit:   # 만약 방문하지 않은 노드라면
            visit.append(node)   # 노드를 방문했음을 표시하고
            stack.extend(graph[node])   # 현재 노드와 연결된 노드를 스택에 추가한다
    return visit
          
          
          
computer = int(input())  
M = int(input())
    
graph = {i: [] for i in range(1, computer + 1)} # 참조한부분 어떻게 입력 받아야할지 몰라서

for _ in range(M):   # 간선의 입력 받기
    u,v = map(int, input().split())
    graph[u].append(v)   # 양방향으로 두 번
    graph[v].append(u)
    
print(dfs(graph,1))  # DFS 결과 출력