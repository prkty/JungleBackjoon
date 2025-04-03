# 미로에서 1은 갈 수 있는 칸이고 0은 갈수 없다.
# 1,1에서 최종목적지까지 몇번째 칸을 지나야 최종 목적지 갈 수 있는지 알아내는 문제이다.
# BFS와 다익스트라 방식으로 풀 수 있다.
import sys
import heapq

input = sys.stdin.readline

# 입력 받기
N = int(input().strip())  # 방의 크기
graph = [list(map(int, list(input().strip()))) for _ in range(N)]  # 미로 입력

# 방향 이동 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 방문 처리 및 최소 비용 저장 (INF로 초기화)
INF = float('inf')
cost = [[INF] * N for _ in range(N)]
cost[0][0] = 0  # 시작점은 바꾸지 않으므로 비용 0

# 다익스트라를 위한 우선순위 큐 사용
pq = []
heapq.heappush(pq, (0, 0, 0))  # (비용, x좌표, y좌표) 비용이 작은 순으로 탐색

# 힙큐가 없을 때까지
while pq:
    curr_cost, x, y = heapq.heappop(pq)  # 현재 비용이 가장 작은 위치를 가져옴

    # 이미 저장된 값보다 크다면 무시(최단 거리 구하므로)
    if curr_cost > cost[x][y]:
        continue

    # 네 방향 탐색
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]  # x 좌표 상하이동, y 좌표 좌우이동

        if 0 <= nx < N and 0 <= ny < N:  # 정해진 N 범위 내에 있는 경우
            new_cost = curr_cost + (1 if graph[nx][ny] == 0 else 0)  # 검은 방이면 +1
            # 현재값 + (이동한 그래프 좌표가 0(검은방)이면 1반환, 그외에는 0반환)

            # 기존 비용보다 새로운 비용이 더 적으면 갱신(검은방을 바꾸는 최소 비용을 찾음)
            if new_cost < cost[nx][ny]:
                cost[nx][ny] = new_cost  # 구한 값은 cost에 입력(갱신)
                heapq.heappush(pq, (new_cost, nx, ny))  # 우선순위 큐에 삽입(다른 경우 수 확인)

# 도착지점의 최소 변경 횟수 출력
print(cost[N-1][N-1])  # N이 8이더라도 좌표상 7,7이므로 N-1을 한다.

# 기존의 BFS를 사용하면 금방 작성할 줄 알았는데 생각보다 오래걸렸다
# 이 문제가 검은 방을 만났을때 처리할 방법에 대해 궁금했는데
# BFS랑 다익스트라랑 같이 써서 전체의 비용을 조사하면서 제일 작은 값을
# 계속 갱신하여 최솟값을 구한다는 생각이 키포인트인 것 같다.
# 코드도 난해해서 이해를 좀 더 해봐야겠다.
