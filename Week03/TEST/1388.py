# 같은 행일때 같게 치면 근처(왼,우) 스캔해서 같은 값이면 하나로 치면 될 것 같음
# 순회하면서 같은거 나오면 한개로치고 아니면 따로 셈
import sys

input = sys.stdin.readline

# 방 바닥의 세로 크기 N, 가로 크기 M
N,M = map(int, input().split())
graph = [] 	# 2차원 리스트의 맵 정보 저장할 공간
for _ in range(N):
    graph.append(list(input()))

# -나무
count = 0
for i in range(N):
    a = ''
    for j in range(M):
        if graph[i][j] == '-':   # -일시
            if graph[i][j] != a:
                count += 1
        a = graph[i][j]   # 만약에 -이면 같은 걸로 계산, 다른게 나오면 상단에 if에 따라 다른 걸로 계산

# ㅣ나무
for j in range(M):
    a = ''
    for i in range(N):
        if graph[i][j] == '|':  # |일시
            if graph[i][j] != a:
                count += 1
        a = graph[i][j]
        

print(count)