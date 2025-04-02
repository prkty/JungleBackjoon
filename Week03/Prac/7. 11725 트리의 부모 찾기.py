# 트리들이 구현되어 있을때, 각각 노드의 부모를 구하는 문제이다.
# DFS 돌려서 부모와 자식 관계 맞으면 부모정보를 내보내면된다.
# 이렇게 되기 위해서는 부모 리스트를 따로 관리해야되고 2부터 7까지 차례대로
# 출력되야해서 까다롭다.
import sys

input = sys.stdin.readline

def dfs(graph, start, N):
    stack = [(start, 0)]  # 스택 초기화 (현재 노드, 부모 노드)
    parent_node = [0] * (N + 1)  # 부모 노드 저장 리스트 (1-based index)
    
    while stack:
        node, parent = stack.pop()   # 스택에서 현재 노드와 부모 노드 추출
        
        if parent_node[node] == 0:  # 아직 부모가 정해지지 않은 경우
            parent_node[node] = parent   # 현재 노드의 부모 저장
            
            for next_node in graph[node]:
                if parent_node[next_node] == 0:  # 아직 방문하지 않은 노드만 추가
                    stack.append((next_node, node))  # (자식 노드, 부모 노드) 형태로 저장
            
    return parent_node
    


N = int(input())

graph = {i:[] for i in range(1, N+1)}

for _ in range(N-1):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
result = dfs(graph, 1, N) # 루트 노드 1번으로 DFS 실행 result엔 부모노드 N값이 들어감

for i in range(2, N+1):  # 2번 노드부터 부모 출력
    print(result[i])
    
# 난 기존 DFS에서 활용해서 답을 도출해낼 수 있을 줄 알았는데, 일부분이 바껴서 놀랐다.
# 자력으로 풀어보곘다고 시간투자좀 했는데, 첨부터 찾아볼걸 그랫나보다... 