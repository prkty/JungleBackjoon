# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하면된다.
# 나는 직접 경우의 수를 적어보았다. 해보니 퀸은 같은 행과 열에 있으면 안된다.
# 그러기 위해서는 퀸은 한  행이나 열에 한개씩은 있어야함을 의미합니다.
# 근데, 대각선은 어떻게 처리를 하는지 아이디어가 떠오르지 않는다.
# N=5까지 확인해보니 경우의 수는 10이다. 나느 1번 퀸을 고정하고 나머지 인자를 옮기면서 조사했다.
# 1,1지점의 1번퀸에서 경우의 수가 다 나오면 1,2로 옮겨서 스캔하고 옆으로 옮겨서 다시스캔하는 방식으로 했다.
# 뭔가 이 재스캔하는 방법을 재귀 알고리즘으로 짜면 될 것 같은데, 어떻게 시작할 지 아직 모르겠다.
# 하는 방식이 N 개에 해당되는 리스트를 모두 0으로 채운다.
# 이후 만약에 퀸을 놓지 못하는 부분이면 1로 바꾼다.
# 오른쪽 상하단으로 지나가는 것은 i+j일때이고, 왼쪽 상하단으로 지나갈 때는 i-j가 일정할 때이다.
# 지나가지 못하는 경우의 수를 lookup 테이블로 해서 
# N = 전체행 번호
# n = 현재행 번호
# 전체 행의 시작이 0,0에서 시작하므로 마지막 줄은 n-1이다.
# n = N 이라면 결과에 +1을 한다. 
# V1 = 열인 j의 해당되며 열의 위치를 표시한다. 해당 열에 해당되지 않게 설정하기 위해 사용한다.
# V2 = 오른쪽 대각선인 i + j에 대해 표시한다.
# V3 = 왼쪽 대각선인 i - j가 일정한 것에 대해 표시한다.
# V1,2,3에 해당하는 칸을 1로 바꾼다.
# lookup 테이블 참조를 통해서 구현한다. V1, V2, V3를 빠르게 공제
# 만약 칸에 0이라면 모든 조건에 만족하는 경우이다.

# 일단 해당 문제의 N 입력단을 쓴다.
def dfs(n):
    global ans
    if n == N:
        ans+=1
        return
    
    for j in range(N):
        if V1[j] == V2[n+j] == V3[n-j] == 0:
            V1[j] = V2[n+j] = V3[n-j] = 1
            dfs(n+1)
            V1[j] = V2[n+j] = V3[n-j] = 0
        
        
N = int(input())

ans = 0 # 나중에 답이 될 ans은 0으로 초기화한다.
 
V1 = [0] * N
V2 = [0] * (2*N)  # 대각선 계산 오른쪽위
V3 = [0] * (2*N)  # 대각선 계산 왼쪽위

dfs(0)
print(ans)












from typing import MutableSequence

def qsort(a: MutableSequence, left: int, right: int) -> None:
    """a[left] ~ a[right]를 퀵 정렬"""
    pl = left                   # 왼쪽 커서
    pr = right                  # 오른쪽 커서
    x = a[(left + right) // 2]  # 피벗(가운데 요소)

    while pl <= pr:    # 실습 6-10과 같은 while 문
        while a[pl] < x: pl += 1   # 내림차순 시 교체 대상
        while a[pr] > x: pr -= 1   # 내림차순 시 교체 대상
        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    if left < pr: qsort(a, left, pr)
    if pl < right: qsort(a, pl, right)

def quick_sort(a: MutableSequence) -> None:
    """퀵 정렬"""
    qsort(a, 0, len(a) - 1)

if __name__ == '__main__':
    print('퀵 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num   # 원소 수가 num인 배열을 생성

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    quick_sort(x)      # 배열 x를 퀵 정렬

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
















