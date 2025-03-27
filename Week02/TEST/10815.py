# N과 M 비교해서 맞으면 1 틀리면 0
import sys

N_num = int(input())
N = sorted(list(map(int,sys.stdin.readline().strip().split())))

M_num = int(input())
M = list(map(int,sys.stdin.readline().strip().split()))

def bin_search(N,key):
    pl = 0          
    pr = len(N) - 1  
    
    while pl <= pr:      

        pc = (pl + pr) // 2   # 중앙 지정
        if N[pc] == key:      # 키랑 pc랑 같으면 찾음
            return pc         # pc값을 리턴
        
        elif N[pc] < key:     # 키값이 크면
            pl = pc + 1       # 오른쪽 범위로 이동(인덱스)
            
        else:
            pr = pc - 1       # 키 값이 작으면 왼쪽 범위로 이동(인덱스)
        
    return -1  # 종료(결과에 없음)
    
# 이진 탐색 수행 및 결과 출력
for key in M:   # 한 개씩 돌아가면서 비교
    result = bin_search(N, key)   # 입력 받은 값을 대입
    print(1 if result != -1 else 0)  # 만약 -1이 아니라면 1, -1이면 리스트에 없으므로 0 출력
    
    
# 해당 문제가 해시로 푸는 것이 더 좋다고 한다.
# 해시는 set과 딕셔너리가 있는데, 특히 set을 쓰면 빠르게 풀수 있다.(5줄)