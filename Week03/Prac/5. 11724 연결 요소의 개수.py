# 해당 문제는 몇개의 그래프가 있는지 묻는 문제와 같다
# M만큼 입력을 받는다
# 리스트를 만들어서 그래프를 만들고
# 기존 그래프에 해당되지 않은 정렬이면, 그래프 하나 만들면서 count +1
# 재귀적으로 반복 후에 count만 내보낸다. 라는게 내 생각이다.

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한 증가

N, M = map(int, input().split())

graph = [[False] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u][v] = True
    graph[v][u] = True

    
def dfs(idx) :
    global visited   # 방문기록을 지역변수로 불러옴
    visited[idx] = True   # 정점의 방문기록 True
    # print(idx, end = ' ')  # 정점을 출력
    for next in range(1, N+1) :   # 인덱스 1부터 끝까지 순회하며 확인 
        if not visited[next] and graph[idx][next]:  # 방문하지 않았고 간선이 존재하는 정점이라면
            dfs(next)   # dfs에 재귀적으로 입력 
            
# 연결요소 카운팅
count = 0
for i in range(1, N+1):
    if not visited[i]:
        dfs(i)
        count += 1
    
    
print(count)

# dfs를 구현하는 건 전 문제를 참고하여 구현했는데,
# 연결 요소 카운팅을 어떻게 해야되나 고민을 많이 했다.
# dfs 자체도 건드리고 방법을 강구하다가 gpt에 물어 봤더니 생각보다 간단했다.
# for문으로 전체 요소에 방문정보가 False가 있으면 dfs를 다시 한번 호출하며 카운트를 1 올리는 방법이었다.