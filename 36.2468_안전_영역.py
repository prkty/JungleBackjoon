# 해당 문제는 물에 잠기는 정도를 조절하며 안전 영역이 최대한으로 많이 생길 때를 탐색한다.
# 내가 안전영역의 개념이 헷갈렸는데 동료분의 설명으로 바로 이해했다. 
# 이어져 있는 침수되지 않은 부분은 여러개더라도 1개의 안전지대로만 인정한다. 모서리는 제외
# 모든 경우의 수를 생각해야하므로 DFS 깊이우선탐색 방식으로 구현해야한다.
# 그러나 DFS는 나중에 배우니 DFS없이 구현해보겠다. 시간 관계상 GPT의 도움을 받았다.

import sys
input = sys.stdin.readline

# 입력 받기
N = int(input())  # 지역 크기
grid = [list(map(int, input().split())) for _ in range(N)]  # 높이 정보

max_height = max(map(max, grid))  # 지역 내 최고 높이 찾기
max_safe_areas = 0  # 최대 안전 영역 개수 저장

# 모든 높이에 대해 안전 영역 개수 찾기
for height in range(0, max_height + 1):  # 비 높이를 0부터 최대 높이까지 조절
    visited = [[False] * N for _ in range(N)]  # 방문 배열 초기화
    safe_areas = 0  # 현재 높이에서 안전 영역 개수

    # 모든 지역을 순회하며 안전 영역 찾기
    for i in range(N):
        for j in range(N):
            if grid[i][j] > height and not visited[i][j]:  # 침수되지 않은 곳이고 방문하지 않았다면
                # DFS 없이 직접 하나의 안전 영역을 모두 방문 처리
                stack = [(i, j)]  # 방문할 위치 저장
                while stack:
                    x, y = stack.pop()  # 현재 위치 가져오기
                    visited[x][y] = True  # 방문 처리

                    # 상하좌우 탐색
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < N:  # 범위 내에 있고
                            if not visited[nx][ny] and grid[nx][ny] > height:
                                visited[nx][ny] = True  # 방문 처리
                                stack.append((nx, ny))  # 새로운 위치 추가
                
                safe_areas += 1  # 하나의 안전 영역 탐색 완료

    max_safe_areas = max(max_safe_areas, safe_areas)  # 최대값 갱신

# 결과 출력
print(max_safe_areas)
