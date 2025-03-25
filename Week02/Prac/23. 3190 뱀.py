# 고려할 사항이 여러가지다. 

import sys
from collections import deque

# 1. 입력 받기
N = int(sys.stdin.readline().strip())  # 보드 크기
K = int(sys.stdin.readline().strip())  # 사과 개수
board = [[0] * N for _ in range(N)]  # 보드 초기화 (0: 빈 칸, 1: 사과)

# 2. 사과 위치 입력
for _ in range(K):
    x, y = map(int, sys.stdin.readline().split())
    board[x - 1][y - 1] = 1  # 1-based → 0-based로 변환

# 3. 방향 변환 정보 입력
L = int(sys.stdin.readline().strip())  # 방향 변환 개수
turns = {}  # {X초: "L" 또는 "D"}
for _ in range(L):
    X, C = sys.stdin.readline().split()
    turns[int(X)] = C

# 4. 방향 관련 변수 (오른쪽 → 아래 → 왼쪽 → 위쪽)
dx = [0, 1, 0, -1]  # X 변화량 (동, 남, 서, 북)
dy = [1, 0, -1, 0]  # Y 변화량 (동, 남, 서, 북)
direction = 0  # 초기 방향 (오른쪽)

# 5. 뱀의 몸을 관리할 큐
snake = deque([(0, 0)])  # 초기 위치
time = 0  # 게임 시간

# 6. 게임 루프
while True:
    time += 1  # 1초 증가
    head_x, head_y = snake[-1]  # 현재 머리 위치

    # 다음 이동 위치 계산
    new_x = head_x + dx[direction]
    new_y = head_y + dy[direction]

    # 7. 게임 종료 조건 (벽 또는 몸과 부딪힘)
    if new_x < 0 or new_x >= N or new_y < 0 or new_y >= N or (new_x, new_y) in snake:
        break

    # 8. 이동 수행
    snake.append((new_x, new_y))  # 머리 이동

    if board[new_x][new_y] == 1:  # 사과가 있으면
        board[new_x][new_y] = 0  # 사과 제거 (몸 길이 유지)
    else:  
        snake.popleft()  # 사과 없으면 꼬리 이동 (길이 유지)

    # 9. 방향 전환 확인
    if time in turns:
        if turns[time] == "L":  # 왼쪽 회전
            direction = (direction - 1) % 4
        else:  # 오른쪽 회전
            direction = (direction + 1) % 4

# 10. 결과 출력
print(time)
