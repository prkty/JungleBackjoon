# 기본적으로 그래프를 구현하고 방문했는지 알기 위한 visited가 있어야한다.
# 2차원 배열을 만들어서 모두 False처리하고 입력값에 따라 True로 받는다
# dfs는 검색지점을 계속 옮기며 재귀함수로 실행하며 깊이 우선 탐색을 하고
# bfs는 첫 정점에서 갈 수 있는 곳을 큐에 저장하여 큐가 모두 소진할 때까지 진행한다.

import sys

def dfs(idx) :
    global visited   # 방문기록을 지역변수로 불러옴
    visited[idx] = True   # 정점의 방문기록 True
    print(idx, end = ' ')  # 정점을 출력
    for next in range(1, N+1) :   # 인덱스 1부터 끝까지 순회하며 확인 
        if not visited[next] and graph[idx][next]:  # 방문하지 않았고 간선이 존재하는 정점이라면
            dfs(next)   # dfs에 재귀적으로 입력

def bfs():
    global q, visited  # 방문기록, 큐를 지역변수로 불러옴
    while q:   # 큐가 빌때까지 실행
        cur = q.pop(0)  # 현재 큐 중에 맨 앞 큐를 pop한 것을 cur에 저장
        visited[cur] = True   # 방문을 True로 바꿈
        print(cur, end = ' ')  # cur을 차례대로 출력
        for next in range(1, N + 1) :  # 인덱스 1부터 끝까지 순회하며 확인
            if not visited[next] and graph[cur][next]:  # 방문하지 않았고 간선이 존재하는 정점이라면
                visited[next] = True   # 다음 방문할 곳을 방문했다고 표시
                q.append(next)   # 다음 방문지를 큐에 저장

# 0. 입력 및 초기화
input = sys.stdin.readline
N, M, V = map(int, input().split())  # 입력값 받음
# N은 정점의 총 개수, M은 간선의 총 개수, V는 첫 정점

graph = [[False] * (N + 1) for _ in range(N + 1)]  # 그래프를 N*N만큼 2차원 배열로 표현(초기는 모두 Flase)
visited = [False] * (N + 1)   # 방문자도 N만큼 Flase로 지정

# 1. graph 정보 입력
for _ in range(M) :
    a, b = map(int, input().split())
    graph[a][b] = True  # 입력된 좌표는 갈 수 있음을 표시
    graph[b][a] = True  # 입력된 좌표는 갈 수 있음을 표시

# 2. dfs 
dfs(V)
print()

# 3. bfs
visited = [False] * (N + 1)  # 방문자도 N만큼 Flase로 지정
q = [V]  # Q에 초깃값 입력
bfs()

# 이론은 알기에 수월했는데 코드로 구현은 이해할 듯하는데 코드로 구현하긴 어려운 것 같다
# 생각보다 코드가 간단했지만, 디테일한 부분이 있어서 이해하기 좀 어려웠다.