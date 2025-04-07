# LCS(Subsequence)은 부분수열로 문자사이를 건너뛰면서 두 문자의 공통이면서 가장 긴 부분 문자열을 찾으면 됩니다.
# 만약 ABCDEF와 GBCDFE일 경우 BCDF가 LCS가 됩니다.
# 참고로 LCS의 마지막 글자인 Subsequence는 건너뛰기가 되고(부분수열)
# Substring은 건너뛰기가 안됩니다.(이어진 문자만)

# LCS관련 문제는 2차원 배열을 만들어서 두 문자를 비교해서 동일하면 표기하는 방식으로
# 계산함을 알게 되었습니다.
import sys 
input =  sys.stdin.readline

A = input().strip()
n = len(A)   # 6
B = input().strip()
m = len(B)   # 6

dp = [[0] * (m + 1) for _ in range(n + 1)]  # 7 * 7

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if A[i - 1] == B[j - 1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
print(dp[n][m])
# 이게 문제 원리는 이해하기 쉬웠는데, 코드 전개가 굉장히 헷갈렸다.
# 공백을 넣어서 비교하는데에 예외사항이 생기지 않게 해야되고
# 함수에 -1과 +1을 번갈아 써서 굉장히 헷갈렸다.
# 그런데 A[]를 각 알파벳을 가르키는 숫자라고 생각하니 이해하기 한결 쉬웠다.