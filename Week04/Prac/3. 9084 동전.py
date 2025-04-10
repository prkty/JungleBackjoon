# 이문제는 살펴보니 목표 금액을 기준으로 점화식을 도출해 내면된다. 
# 이건 직접 경우의 수를 계산해보면 점화식을 이끌어내기 수월하다.
# 동전이 추가될 때마다 증가되는 경우의 수가 일정하다.
# 헤딩 규칙을 살려서 결론을 도출하면된다.
import sys

input = sys.stdin.readline

def coin_dp(coin, M):
    dp = [0] * (M+1)
    dp[0] = 1
    
    for coin in coins:  # 각 동전에 대해
        for i in range(coin, M + 1):
            dp[i] = dp[i] + dp[i - coin]
            # 해당 수식이 점화식을 말한다. 동전 수가 추가될 때마다 경우의 수가 증가된다.
    return dp[M]
    
T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    coins = list(map(int, input().strip().split()))
    M = int(input().strip())
    
    print(coin_dp(coins, M))
    
# 코인을 추가하면 dp[i - coin]만큼의 새로운 방법이 추가된다.