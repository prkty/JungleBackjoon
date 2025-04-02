# 미로에서 1은 갈 수 있는 칸이고 0은 갈수 없다.
# 1,1에서 최종목적지까지 몇번째 칸을 지나야 최종 목적지 갈 수 있는지 알아내는 문제이다.
from collections import deque
import sys

input = sys.stdin.readline

def BFS(start_x, start_y, end_x, end_y, graph):
    """BFS를 사용하여 최단 거리를 탐색하는 함수"""
    # 상하좌우 이동을 위한 방향 벡터를 설정합니다.
    # dx, dy를 활용하면 for문을 돌며 이동 좌표를 한 번에 계산할 수 있습니다.
    dx = [-1, 1, 0, 0]  # 상, 하 이동
    dy = [0, 0, -1, 1]  # 좌, 우 이동
    
    visited = set([(start_x, start_y)])   # 방문한 노드를 기록하는 집합 (x, y) 형태로 저장
    # visited로 중복 방문을 방지
    queue = deque([(start_x, start_y, 1)])  # (현재 위치 x, y, 이동 거리(1씩이동))

    while queue:  # 큐가 빌때까지 실행
        x, y, steps = queue.popleft()  # 현재 위치와 이동 거리 꺼내기

        if x == end_x and y == end_y:  # 도착 지점에 도달하면
            return steps  # 최단 거리 반환

        for i in range(4):  # 상하좌우 이동
            nx = x + dx[i]  # 현재 x에서 dx만큼 이동
            ny = y + dy[i]  # 현재 y에서 dy만큼 이동

            # 범위를 벗어나지 않고 방문하지 않은 길(1)인 경우 이동
            if 0 <= nx < N and 0 <= ny < M:   # 입력된 N, M에 따라 범위를 벗어나지 않게 한다.
                if (nx, ny) not in visited and graph[nx][ny] == 1:  # 방문하지 않았고 1인 지역이면
                    visited.add((nx, ny))  # 방문 기록 추가
                    queue.append((nx, ny, steps + 1))  # 이동 거리 증가하여 추가

    return -1  # 도착점까지 도달할 수 없는 경우

# 입력 처리
N, M = map(int, input().split())  # 미로 크기 입력
graph = [list(map(int, list(input().strip()))) for _ in range(N)]  # 미로 정보 (숫자로 변환)

# BFS 실행 및 결과 출력
print(BFS(0, 0, N-1, M-1, graph))  # (0,0)에서 (N-1,M-1)까지 최단 거리 탐색
# N이 4라고 하면 인덱스로는 3까지라서 N-1을 한다.

# BFS의 제일 기초문제인데도 코드 해석하는데 오랜시간이 걸렸다. DFS랑 다르게 위와 같은 2차원 배열에서는
# 처리하기가 굉장히 어려운 것 같다. 오늘은 3시경까지 공부하느라 늦어서 내일 아침에 다시한번 이해하겠다.
# 앞으로는 위의 식을 활용하여 여러 BFS 문제를 풀어보겠다.




# from collections import deque
# import sys

# input = sys.stdin.readline

# # 방향 벡터 (상, 하, 좌, 우)
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

# def bfs(x, y):
#     """BFS를 사용하여 최단 거리를 탐색하는 함수"""
#     queue = deque()
#     queue.append((x, y))  # 시작 위치 삽입

#     while queue:
#         x, y = queue.popleft()  # 큐에서 꺼내기

#         for i in range(4):  # 상하좌우 이동
#             nx = x + dx[i]
#             ny = y + dy[i]

#             # 미로 범위를 벗어나면 무시
#             if nx < 0 or nx >= N or ny < 0 or ny >= M:
#                 continue

#             # 벽(0)이면 무시
#             if maze[nx][ny] == 0:
#                 continue

#             # 처음 방문하는 곳이면 거리 업데이트 후 큐에 추가
#             if maze[nx][ny] == 1:
#                 maze[nx][ny] = maze[x][y] + 1  # 거리 갱신
#                 queue.append((nx, ny))  # 이동 가능 위치 추가

#     return maze[N-1][M-1]  # 도착 지점의 값 반환 (최단 거리)

# # 입력 처리
# N, M = map(int, input().split())  # 미로의 크기
# maze = [list(map(int, list(input().strip()))) for _ in range(N)]  # 미로 정보

# # BFS 실행 및 결과 출력
# print(bfs(0, 0))