# 해당 문제는 푸는 방식이 두가지 있습니다.
# 파이썬 함수의 combination를 사용해서 수열의 모든 경우의 수 조합으로 우리가 원하는 S에 도달할 때의 개수를 출력하는 방법
# 재귀함수와 백트레킹을 활용하여 0번째 인덱스부터 시작해 n-1번째 인덱스까지 각 원소의 값들을 넣고,
# 해당 값을 지금까지 구해온 sub_sum에 더하는 경우와 더하지 않는 경우를 각 가지로 나누어 재귀함수를 호출합니다.

# combination 방식
import sys
from itertools import combinations  # combination패키지를 불러옵니다

input = sys.stdin.readline    # readline으로 빠르게 입력을 받아옵니다.
n, s = map(int, input().split())    # 입력값을 받습니다.
arr = list(map(int, input().split()))
cnt = 0    # 횟수는 0으로 초기화합니다.

for i in range(1, n+1):  # 첫값부터 N까지 모든 경우의 수를 확인합니다.
    comb = combinations(arr, i)   # combination으로 수열의 모든 조합을 확인합니다. 그러나 순서가 바뀐 것은 같은 취급을 합니다.

    for x in comb:    # 조합이 맞을 시 처리
        if sum(x) == s:   # x즉 수열의 수의 합이 입력된 s와 값이 같다면
            cnt += 1   # 부분수열의 개수를 +1 합니다.

print(cnt)   # 결과를 출력합니다.


# 재귀와 백트래킹 방식
import sys

input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

def subset_sum(idx, sub_sum):   # 재귀를 위한 함수입니다.
    global cnt  # 지역변수로 횟수를 불러옵니다.

    if idx >= n:   # 
        return

    sub_sum += arr[idx]

    if sub_sum == s:   # 요소의 조합이 조건에 맞을시 처리
        cnt += 1    # 부분수열의 개수를 +1 합니다.
    
    # 현재 arr[idx]를 선택한 경우의 가지 수
    subset_sum(idx+1, sub_sum)

    # 현재 arr[idx]를 선택하지 않은 경우의 가지 수
    subset_sum(idx+1, sub_sum - arr[idx])

subset_sum(0, 0)
print(cnt)