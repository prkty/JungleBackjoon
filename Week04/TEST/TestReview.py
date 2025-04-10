import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if board[i][j] == 0:
            continue

        val = board[i][j]
        dx = [val, 0]
        dy = [0, val]

        for k in range(2):
            ni = i + dx[k]
            nj = j + dy[k]

            if 0 <= ni < n and 0 <= nj < n:
                dp[ni][nj] += dp[i][j]

print(dp[n-1][n-1])