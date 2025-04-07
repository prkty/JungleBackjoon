import sys
input = sys.stdin.readline

A = input().strip()
B = input().strip()

n = len(A)
m = len(B)

# dp[i][j]는 A[i-1]와 B[j-1]에서 끝나는 공통 문자열의 길이
dp = [[0] * (m + 1) for _ in range(n + 1)]

max_length = 0  # 최장 공통 문자열의 길이 저장

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if A[i - 1] == B[j - 1]:  
            # 연속되는 문자열이므로 이전 dp[i-1][j-1]에 1 추가
            dp[i][j] = dp[i - 1][j - 1] + 1
            max_length = max(max_length, dp[i][j])  # 최댓값 갱신
        else:
            dp[i][j] = 0  # 연속되지 않으면 끊김

print(max_length)
