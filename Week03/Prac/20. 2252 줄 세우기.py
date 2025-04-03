# N 명의 학생을 M만큼 비교해서 줄세운 결과를 출력하면 된다.
# 위상정렬로 순서를 나타내면 된다. 특성상 답이 여러개 있는데 아무거나 출력할 수 있다.
# 위상정렬을 구현해서 풀면된다.
# 주요 포인트는 디그리를 관리하는 리스트와 정점와 간선을 관리하는 리스트가 있어야한다.
# 큐에 디그리가 0인 정점을 저장하고 결과로 보내고, 빠진 정점은 자식 노드의 디그리를 -1하여
# 해당 과정을 반복하여 위상정렬을 수행한다.
import sys
input = sys.stdin.readline
from collections import deque

# 노드의 개수와 간선의 개수를 입력 받기
N, M = map(int, input().split())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (N + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
# 노드 갯수 N만큼 리스트 만든다
graph = [[] for i in range(N + 1)]

# 방향 그래프의 모든 간선 정보를 입력 받기
for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B) # 정점 A에서 B로 이동 가능
    # 진입 차수를 1 증가(A가 부모고 B가 자손이므로)
    indegree[B] += 1


# 위상 정렬 함수
def topology_sort():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐 기능을 위한 deque 라이브러리 사용(디그리가 0인 정점 저장)

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()  # 디그리 0인 정점 빼서 결과에 넣음
        result.append(now)
        
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    # 위상 정렬을 수행한 결과 출력
    for i in result:
        print(i, end=' ')

topology_sort()

# 위상 정렬 함수를 위에 식이 아니라 다른 식을 써봤는데
# 생각보다 인풋 넣기가 쉽지 않았고 GPT도 이상하게 알려줘서
# 다른 위상정렬 코드를 가져와 풀었다.
# 앞으로도 이 코드를 활용하여 작성해보겠다.