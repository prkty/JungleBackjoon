# 각각의 부품이 요구되는 부품이 있다. 
# 그래서 기본부품  1,2,3,4의 갯수를 구하면 되는 문제인데,
# 이걸 어떻게 위상 정렬로 풀어나가야할지 모르겠다...
# 문제가 사이클이 없고 시작과 종료 지점이 명확하여 위상정렬로 푼다고 합니다.
# 각 부품들이 몇의 가중치로 만들어지는지 그림을 그려보면 이해하기 쉽다.
# 그러면 디그리가 0인 부품을 큐에 넣어서 필요한 부품을 리스트에 넣습니다.
# 가중치에 전에 있던 가중치를 곱해서 완성품까지 필요한 부품수를 추출합니다.

import sys
input = sys.stdin.readline

from collections import deque

N = int(input())
M = int(input())
connect = [[] for _ in range(N + 1)]   # N까지 간선 정보
need = [[0] * (N+1) for _ in range(N + 1)]  # 필요한 부품수
q = deque()  # 위상정렬 실행
degree = [0] * (N+1)  # 진입 차수 0으로 초기화

for _ in range(M):
    X, Y, K = map(int, input().split())
    connect[Y].append((X, K))  # 자식과 가중치로 추가
    degree[X] += 1   # X 디그리는 1씩 추가
    
for i in range(1, N + 1):
    # 인디그리 0인걸 큐에 추가
    if degree[i] == 0:
        q.append(i)
        
while q:   # 큐 내용 소진시 까지 실행
    now = q.popleft()    # 큐에서 왼쪽부터 차례대로 내보냄
    
    # 현재 부품(now)을 이용하여 만들 수 있는 부품들 탐색
    for next, next_need in connect[now]:  # next: 다음 단계 부품 번호, next_need: 현재 부품이 몇 개 필요한지
        
        # 현재 부품이 "기본 부품"인 경우
        if need[now].count(0) == N + 1:  # need[now] 리스트가 모두 0이라면, 즉 기본 부품이라면
            need[next][now] += next_need  # 기본 부품의 개수를 직접 추가
            
        # 현재 부품이 "중간 부품"인 경우
        else:
            for i in range(1, N + 1):  # 1번부터 N번 부품까지 확인
                need[next][i] += need[now][i] * next_need
                # 현재 부품(now)을 만들기 위해 필요한 기본 부품 개수를 이용해 next 부품에 누적(곱함)
                
        degree[next] -= 1   # 진입 차수 감소 (현재 부품을 사용했으므로 next 부품의 필요 조건이 하나 줄어듦)
        if degree[next] == 0:   # 만약 진입 차수가 0이 되었다면 (더 이상 기다릴 필요 없음)
            q.append(next)   # 큐에 추가하여 다음 단계에서 처리
            
# 출력단
for x in enumerate(need[N]):    # need[N]에서 필요한 기본 부품 정보를 가져옴
    if x[1] > 0:   # 만약 해당 부품이 필요하다면(0보다 크다면)
        print(*x)   # 부품 번호와 개수를 출력(리스트 형식 빼고 숫자만 출력)
        
# 블로그를 참조하며 직접 하나하나 클론 코딩하며 학습했다.
# 그림을 그려보며 이론을 이해하긴 했으나 행렬을 구현할 생각을 하지 못했다.
# 기존에 가중치 값에 곱해주므로써 각각의 기본 부품 값을 알 수 있는 것이 놀랍다.
# 솔직히 모든 코드가 이해된 건 아니라서 좀더 이해해보고 다음 문제로 넘어 가겠다.
# 저 중간에 현재 부품과 중간 부품 나눠서 판단하는 for문이 이해하기 좀 어렵다...
