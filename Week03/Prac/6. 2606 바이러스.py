# 해당 문제는 dfs를 실행해서 감염된 컴퓨터 대수를 출력하면된다.
# dfs를 진행하다가 완료될텐데, 그때의 첫 컴퓨터가 연결된 노드만 알면되니까
# 첫 dfs 재귀에서 연결된 노드정보만 받아오면 될 것 같다.
# 입력을 어떻게 받을지 몰라서 GPT를 참조 했다.
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
    
infected_computers = dfs(graph,1)  # dfs를 1번부터 시작

print(len(infected_computers)-1)  # 1번 컴퓨터를 제외한 총 길이 출력

# dfs를 이미 들어간 값에 결과를 뽑아봤지,연결된 노드의 수를 뽑아야되서 고민을 했다.
# 근데 생각보다 간단하게 나온 노드의 수를 len으로 처리해서 쉽게 컴퓨터의 수를 얻을 수 있었다.
# dfs의 노드와 간선 입력값을 받는 방식을 새롭게 알게되었다.