# 문제는 주어진 K원을 만들때 동전의 개수를 최소한으로 출력하고 싶다.
# 그럴려면 K원 한도내에서 제일 큰 동전을 출력해야한다.

import sys
input = sys.stdin.readline

# 그리디 알고리즘
def coin_counter(N, K, coin):
    count = 0
    
    for i in range(N-1, -1, -1):   # range는 stop값 직전까지 반복하여 0까지 반복
        count = count + K // coin[i]  # 몫이 결국 동전의 갯수
        K = K % coin[i]   # 남은 가격 만큼 재계산
    return count

# 입력단
N, K = map(int, input().split())  # N: 동전의 종류, K: 만들 가격
coin = []
for i in range(N):
    coin.append(int(input().strip()))

print(coin_counter(N, K, coin))

# 생각보다 Dp보다 그리디의 코드가 더 간단하다.
# 그러나 생각하기 힘든건 마찬가지이다.