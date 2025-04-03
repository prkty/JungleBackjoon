# 0으로 분리된 단지의 수를 뽑고, 단지의 집의 개수를 오름차순으로 출력해야한다.
from collections import deque
import sys

input = sys.stdin.readline

dx = [-1, 1, 0, 0]  # 상, 하 이동
dy = [0, 0, -1, 1]  # 좌, 우 이동
    
def BFS(start_x, start_y, graph, visited):
    visited[start_x][start_y] = True  # 방문 처리
    # visited로 중복 방문을 방지
    queue = deque([(start_x, start_y)])  # (현재 위치 x, y, 이동 거리(1씩이동))
    count = 1  # 내집

    while queue:  # 큐가 빌때까지 실행
        x, y = queue.popleft()  # 현재 위치 꺼내기

        for i in range(4):  # 상하좌우 이동
            nx = x + dx[i]  # 현재 x에서 dx만큼 이동
            ny = y + dy[i]  # 현재 y에서 dy만큼 이동

            # 범위를 벗어나지 않고 방문하지 않은 길(1)인 경우 이동
            if 0 <= nx < N and 0 <= ny < N:   # 입력된 N, M에 따라 범위를 벗어나지 않게 한다.
                if graph[nx][ny] == 1 and not visited[nx][ny]:    # 방문하지 않았고 1인 지역이면
                    visited[nx][ny] =True  # 방문 기록 추가
                    queue.append((nx, ny))  # 이동 거리 증가하여 추가
                    count += 1  # 단지내 개수 증가

    return count  # 총 단지 크기 반환

# 입력 처리
N = int(input())
graph = [list(map(int, list(input().strip()))) for _ in range(N)]  # 미로 정보 (숫자로 변환)
visited = [[False] * N for _ in range(N)]  # 방문 여부 저장
complex_counts = []  # 단지별 집 개수 저장

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:  # 집이 있고 방문하지 않은 경우
            complex_counts.append(BFS(i, j, graph, visited))  # BFS 실행 후 단지 크기 저장
            
# 결과 출력
complex_counts.sort()  # 단지 크기 오름차순 정렬
print(len(complex_counts))  # 총 단지 수 출력
for count in complex_counts:
    print(count)  # 각 단지 크기 출력