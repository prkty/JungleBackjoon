# 이동할 수 있는 곳: ., 물차있는 곳: *
# 비버굴: D, 고슴도치 위치: S
# 물과 고슴도치는 십자가로 움직인다. 그래서 BFS를 쓴다.
# 돌은 물과 고슴도치가 지나갈 수 없다.

from collections import deque
import sys

input = sys.stdin.read
data = input().split()

# 방향 벡터 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 입력값 처리
R, C = map(int, data[:2])  # R: 행 개수, C: 열 개수
index = 2  # 입력값 리스트에서 지도 데이터의 시작 인덱스(앞의 행과 열 개수 제외)

# 지도 (2차원 리스트) 및 큐 초기화
grid = []  # 지도 저장
water_queue = deque()  # 물 BFS를 위한 큐
hedgehog_queue = deque()  # 고슴도치 BFS를 위한 큐

for r in range(R):
    row = list(data[index])  # 한 줄씩 읽어서 리스트로 변환
    for c in range(C):
        if row[c] == 'S':  # 고슴도치 시작 위치 저장
            hedgehog_queue.append((r, c, 0))  # (행, 열, 현재 이동 시간)
        elif row[c] == '*':  # 물의 위치 저장
            water_queue.append((r, c))  # (행, 열)
    grid.append(row)
    index += 1  # 다음 줄로 이동

# BFS 수행 (물을 먼저 퍼뜨린 후 고슴도치 이동)
def bfs():
    while hedgehog_queue:  # 고슴도치가 이동할 곳이 없을 때까지 반복
        # 1. 물을 먼저 확장
        water_len = len(water_queue)
        for _ in range(water_len):  # 현재 큐에 있는 모든 물 확장
            wx, wy = water_queue.popleft()
            for i in range(4):  # 상하좌우 탐색
                nx, ny = wx + dx[i], wy + dy[i]
                if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] == '.':  # 빈 공간일 경우
                    grid[nx][ny] = '*'  # 물이 퍼짐
                    water_queue.append((nx, ny))  # 새로운 물 위치 큐에 추가

        # 2. 고슴도치 이동
        hedgehog_len = len(hedgehog_queue)
        for _ in range(hedgehog_len):  # 현재 큐에 있는 모든 고슴도치 이동
            hx, hy, time = hedgehog_queue.popleft()
            for i in range(4):  # 상하좌우 탐색
                nx, ny = hx + dx[i], hy + dy[i]
                if 0 <= nx < R and 0 <= ny < C:
                    if grid[nx][ny] == 'D':  # 비버의 굴에 도착한 경우
                        print(time + 1)  # 걸린 시간 출력
                        return
                    if grid[nx][ny] == '.':  # 빈 공간으로 이동 가능
                        grid[nx][ny] = 'S'  # 방문 처리
                        hedgehog_queue.append((nx, ny, time + 1))  # 이동 정보 추가

    # 고슴도치가 비버의 굴까지 갈 수 없는 경우
    print("KAKTUS")

# BFS 실행
bfs()

# 어떤 식으로 전개할지는 이해했지만, 코드는 100퍼센트 이해하진 못했다.
# 솔직히 복습이 우선이라 생각해서 복습을 하고 나중에 이해하겠다.