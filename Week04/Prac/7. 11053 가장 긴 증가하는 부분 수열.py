# 해당문제를 DP로 풀려면, 초깃값0으로 두고
# 배열중 제일 작은값 잡은 다음에 그다음 큰 수 카운팅하면서
# 순회돌고, 그 중에서 가장 큰 수를 출력하면되지 않을까 싶다.
n = int(input())

A = list(map(int, input().split()))

# dp[i]: A[i]까지 고려했을 때 가장 긴 증가하는 부분 수열의 길이
dp = [1] * n  # 처음에는 모두 1로 초기화 (자기 자신만 있는 경우)

# 각 i에 대해 이전 j들을 확인하며 dp 갱신
for i in range(n):
    for j in range(i):
        if A[j] < A[i]:    # A[j] < A[i]일 때만 증가 수열이 가능함
            dp[i] = max(dp[i], dp[j] + 1)       # 기존 dp[i]와 dp[j]+1 중 큰 값으로 갱신
            
            
print(max(dp))
# 내가 생각하는 것과 살짝 다른 방식이다.
# 배열에 초기값을 1로 초기화하고 직전값보다 현재값이 크면 최댓값에 +1을 한다.
# 만약에, 작으면 그대로 1일 것이다.
# 중간에 어떤 값이 나와도 값을 비교해서 가장 큰값을 유지하기 때문에 
# 가장 긴 증가하는 부분 수열의 길이를 출력한다.