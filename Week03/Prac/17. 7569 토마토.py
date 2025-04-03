# 인풋값이 왜 저렇게 되는지 의문이었는데, 2번째 입력이 박스가 두개라서 
# 위에 3줄, 아래 3줄이 다 다른 박스이다. 푸는 과정은
# 입력값을 3차원 리스트에 저장, 익은 토마토를 모두 큐에 넣고 BFS 탐색
# BFS로 상하좌우위아래 돌면서 익힘
# 모든 토마토가 익었는지 확인하고 최소 날짜 출력한다.
from collections import deque
import sys

# 입력 받기 (빠른 입력 사용)
input = sys.stdin.read
data = input().split()

# 방향 벡터 (6방향: 상, 하, 좌, 우, 위, 아래)
# 상자 수가 있기 때문에 위, 아래 개념이 추가된다.
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

# 데이터 파싱
M, N, H = map(int, data[:3])  # data의 첫 세값은 가로(M), 세로(N), 높이(H)
box = []  # 박스 리스트 생성
index = 3  # 실제 토마토상태 기록을 시작하는 위치이다.
queue = deque()

### 3차원 배열 만들기(H,N,M 순)
for h in range(H):  # 층 저장
    floor = []
    for n in range(N):  # 세로 저장
        row = list(map(int, data[index:index + M]))  # 행 구현
        for m in range(M):   # 가로 저장
            if row[m] == 1:   # 행 인덱스 1부터 저장
                queue.append((h, n, m))  # 익은 토마토 위치를 큐에 저장
        index += M   # 다음 가로로 이동
        floor.append(row)  # 층에 행을 추가
    box.append(floor)  # 박스에 층을 추가

# BFS 수행
def bfs():
    while queue:
        z, x, y = queue.popleft()
        for i in range(6):
            nz, nx, ny = z + dz[i], x + dx[i], y + dy[i]   # 근처 스캔(익힘)
            if 0 <= nz < H and 0 <= nx < N and 0 <= ny < M and box[nz][nx][ny] == 0: # 제한되는 범위안이라면
                box[nz][nx][ny] = box[z][x][y] + 1  # 날짜 증가
                queue.append((nz, nx, ny))  # 큐에 날짜 추가

# BFS 실행
bfs()

# 결과 계산
max_days = 0  # 최고 날짜 0으로 초기화
for h in range(H):
    for n in range(N):
        for m in range(M):
            if box[h][n][m] == 0:  # 익지 않은 토마토가 남아있다면 -1 출력
                print(-1)
                exit()
            max_days = max(max_days, box[h][n][m])   
            # 익지 않은 토마토가 남아있는게 아니면 최대날짜 출력

# 최소 일수는 (최댓값 - 1) (초기값이 1이었으므로)
print(max_days - 1 if max_days > 1 else 0)

# 여기는 3차원 배열 만드는 것 자체가 어렵다. 시간이 없는 관계로
# 다음 문제로 넘어가곘다. 추후에 공부할 예정이다.