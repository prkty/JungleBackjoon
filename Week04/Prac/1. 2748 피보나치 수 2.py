# 피보나치 수열이며 그전 값을 다시 불러서 계산하는 방식으로
# 문제를 해결하면됩니다.
import sys

input = sys.stdin.readline

def DP(n):
    # N번째 피보나치 수 저장 리스트 공간
    dp = [0] * (n + 1)
    
    # 초기값 설정
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        
    return dp[n]  # N번째 피보나치 수 반환

# 입력 받기
N = int(input().strip())

# 결과 출력
print(DP(N)) 

# 순서는 리스트 공간을 확보, DP 구현, 인풋 순으로 간다.