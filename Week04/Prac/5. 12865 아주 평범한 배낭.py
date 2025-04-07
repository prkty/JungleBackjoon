# K 값이 증가할 수록, 주어진 물품의 무게에 도달할 때마다. +1씩 추가된다.
# 그전값도 반복된다. 그럼 그전값하고 새로 만들어진 값을 비교해서 가장 큰 값을
# 출력하면 되지 않을까?
# 원래 풀던 for 반복문으로도 풀수 있지만, 이번에는 Top-down 방식을 적용시켜 풀었다.
import sys

sys.setrecursionlimit(10**8)
input = sys.stdin.readline

N, K = map(int, input().split())
# N: 물품의 수, K: 버틸수 있는 무게
items = [tuple(map(int, input().split())) for _ in range(N)]

dp = [[-1] * (K + 1) for _ in range (N + 1)] # -1로 초기화 하여 업데이트 예정

def bagpack(i, w):
    if i == N:  # i가 물품에 수에 도달, 물건이 없음
        return 0
    
    if dp[i][w] != -1:
        return dp[i][w]  # 이미 계산된 값이면 재사용(-1이 기본값인데, -1이 아니면 이미 계산된 값이므로)
    
    weight, value = items[i]
    
    # 현재 물건을 선택하지 않는 경우(다음 물건 고려)
    result = bagpack(i + 1, w)
    
    # 현재 물건을 선택할 수 있다면(무게 초과 안하는 선에서)
    if w + weight <= K:
        result = max(result, bagpack(i + 1, w + weight) + value)  # 가치가 제일 큰것을 고름
        
    dp[i][w] = result
    return result

# 결과 출력
print(bagpack(0,0))

# 해당 방식은 어떤 i번 물건을 고려시
# 현재까지의 무게가 W일때의 얻을 수 있는 최대의 가치를 구합니다.
# 현재까지의 무게와 넣을 물건의 합이 주어진 제한보다 적으면 넣을 수 있고,
# 만약 넣을 수 없을 경우 다음 물건을 고려합니다.
# 이전의 있던 값을 저장하므로 중복되는 계산을 방지합니다.

