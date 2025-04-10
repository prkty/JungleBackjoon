import sys
input = sys.stdin.readline

N = int(input())

board = [list(map(int, input().strip().split())) for _ in range (N)] # 2차원 배열을 만든다.
dp = [[0] * N for _ in range(N)]  # 초깃값으로 0을 넣어준다
dp[0][0] = 1   # 시작지점은 1

for i in range(N):
    for j in range(N):
        if dp[i][j] > 0 and board[i][j]:   # 0보다 크거나 범위 안에 라면 점프 시행
            jump = board[i][j]
            if i + jump < N:   # 세로축 N보다 점프량이 적을시 기존꺼에서 더해서 갱신
                dp[i + jump][j] += dp[i][j]
            if j + jump < N:   # 가로축 N보다 점프량이 적을시 기존꺼에서 더해서 갱신
                dp[i][j + jump] += dp[i][j]
                
print(dp[N-1][N-1])