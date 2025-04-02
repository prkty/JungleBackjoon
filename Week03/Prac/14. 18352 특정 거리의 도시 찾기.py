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