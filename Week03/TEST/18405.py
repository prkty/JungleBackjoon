from collections import deque
import sys

input = sys.stdin.readline

# 방향 벡터 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 입력 처리
N, K = map(int, input().split())  # 시험관 크기 (N x N) 및 바이러스 종류 개수
graph = []  # 시험관 정보를 저장할 리스트
virus_list = []  # (바이러스 번호, 행, 열, 시간)을 저장할 리스트

# 시험관 정보 입력 받기
for i in range(N):
    row = list(map(int, input().split()))
    graph.append(row)
    for j in range(N):
        if row[j] != 0:  # 바이러스가 있는 경우
            virus_list.append((row[j], i, j, 0))  # (바이러스 종류, x, y, 시간) 저장

# 낮은 번호의 바이러스가 먼저 확산되도록 정렬
virus_list.sort()

# 큐에 초기 바이러스 정보 삽입
queue = deque(virus_list)

# S초 후 확인할 위치 (X, Y)
S, X, Y = map(int, input().split())

# BFS 실행
while queue:
    virus, x, y, time = queue.popleft()

    # S초가 지나면 종료
    if time == S:
        break

    # 상하좌우 이동하며 전파
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        # 범위를 벗어나지 않고, 아직 감염되지 않은 경우 (0인 경우)
        if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 0:
            graph[nx][ny] = virus  # 바이러스 전파
            queue.append((virus, nx, ny, time + 1))  # 시간 증가하여 큐에 추가

# 결과 출력 (X, Y는 1-based index이므로 0-based로 변환)
print(graph[X-1][Y-1])
