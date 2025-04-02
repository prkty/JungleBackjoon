# 이분 그래프가 무엇인지 모르겠고, 코드 작성에 어려움이 있어
# 블로그를 참고했습니다.
# 이분 그래프를 판단하기 위해서는 각 노드들을 이웃 노드들과 다른 색으로 계속 칠해
# 나가면서, 같은 색의 정점이 서로 연결되어 있는 모순이 발생하는지 여부를 확인하면 된다.
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

K = int(input())  # 테스트 케이스

def dfs(start, group):
    global error  # 에러처리를 전역 변수로 불러옴

    # 만약 사이클이 true라면 재귀탈출
    if error:
        return

    visited[start] = group  # 해당 그룹으로 등록

    for i in graph[start]:
        if not visited[i]:
            dfs(i, -group)  # 다른 그룹으로 설정
        elif visited[start] == visited[i]:  # 인접한데 같은 그룹이라면
            # 이분 그래프는 인접하고 다른 그룹이어야함
            error = True  # 에러값 True
            return  # 그후 재귀 리턴

for _ in range(K):   # 테스트 케이스 만큼 반복
    V, E = map(int, input().split())  # V:정점 개수, E:간선 개수
    graph = [[] for _ in range(V + 1)]  # 빈 그래프 생성
    visited = [False] * (V + 1)  # 방문한 정점 체크
    error = False

    for _ in range(E):   # 입력된 값을 그래프에 추가(양방향)
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, V + 1):
        if not visited[i]:  # 만약 아직 방문하지 않았다면
            dfs(i, 1)  # dfs를 돈다.
            if error:  # 만약 에러가 참이라면
                break  # 탈출
    
    if error:
        print("NO")
    else:
        print("YES")
        
# 이 문제가 인풋이 복잡해서 어떻게 입력되고 그림으로 그려지는지 아는 것이 좋다
# 직접해보며 왜 Yes와 No가 나오는지 알아야 풀 수 있다.
# 그렇다고 코드가 쉬운건 아니라서 오려운 문제라고 생각된다.
# 어느정도 이해하고 다음 문제로 넘어 가겠다.
