# 문제는 분할 정복을 통해 색종이가 파란색과 흰색인 부분의 갯수를 찾는 것이 목표이다.
# 일일이 세는 것은 굉장히 오래걸리기 때문에 분할정복과 재귀를 사용한다.
# 주 핵심은 전체적인 검사를 통해 같은 색이 아니라면 4등분을 합니다. 그후 다시 재귀호출합니다.
# 나눠진 상태에서 같은 색인지 확인하고 아니라면 4등분을 다시하고 재귀호출합니다.
# 나눠진 상태에서 색이 같다면 해당 색을 +1 합니다.
# 나눌수 없는 범위까지 나누면 색이 완벽히 나눠질 것이다.
# 해당 상태에서 최종적인 흰색과 파란색의 갯수를 출력한다.

import sys

# 인풋받기
N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # 색종이 만들기

# 결과 담을 리스트
result = []

def solution(row, col, N) :
    color = paper[row][col]   # 첫번째 칸의 색상 저장(기준)
    for i in range(row, row+N):   # i는 x부터 x+N(끝까지) 검사
        for j in range(col, col+N):     # j는 y부터 y+N(끝까지) 검사
            if color != paper[i][j]:     # 기준값과 현재 검사중인 좌표값이 다를때 분할 시행
                solution(row, col, N//2)        ### 왼쪽위 2사분면 분할
                solution(row, col+N//2,N//2)    ### 오른쪽위 1사분면 분할
                solution(row+N//2, col, N//2)   ### 왼쪽 아래 3사분면 분할
                solution(row+N//2, col+N//2, N//2)    ### 오른쪽 아래 4사분면 분할
                return
            
    # 모든 칸이 같은 색이면 각각의 색상 카운트를 증가
    if color == 0:
        result.append(0)
    else:
        result.append(1)
       
        
solution(0,0,N)    # 0,0 지점부터 재귀 호출 시작
print(result.count(0))   # 각 색깔별로 갯수 출력
print(result.count(1))

# 이론은 어느정도 이해가 간다. 분할된 곳이 같은 색만 나올때까지 재귀 분할 하는 논리이다.
# 그런데 코드에 나누는 식이 이해가 잘 되지는 않는다. 대강 어떤 느낌인지는 알겠는데...
# 일단 넘어가고 복습시 다시 보는 걸로 하겠다.