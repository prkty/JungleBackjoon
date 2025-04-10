# 2, 5만 써서 거스름돈에 맞게 거실러 줘야한다.
# 포인트는 큰 수 부터 돌아가면서 동전의 개수는 최소가 되게끔하는 것이다.
# 그러면 그리디가 적합할 것이다.
import sys

input = sys.stdin.readline

n = int(input())
coin = [5, 2]

def coin_cnt(n, coin):
    count = 0
    # 0 예외사항 처리
    if n == 0:
        return 0
    
    for i in range(n // coin[0], -1, -1):   # coin[0] = 5
        remain = n - coin[0] * i   # 5를 최대한 뺌
        if remain % coin[1] == 0:    # 2로 나눈 나머지가 0일때
            return i + (remain // coin[1])   # 기존의 5의 몫과 2의 몫을 더한값을 리턴
        
    return -1   # 나누지 못했을때 예외처리

print(coin_cnt(n, coin))