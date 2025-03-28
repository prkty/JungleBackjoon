# 문제를 읽고 내가 이해한 것은 여행 경로를 짜야하는데, 한 출발점에서 시작하여 N개의 여행지를 거치고 다시 출발점으로 와야된다.
# 갔던 여행지는 다시 갈 수 없고 수 많은 경로에서 제일 최단 경로를 짜는 것이 이 문제의 핵심이다.
# 그러나 어떻게 코드로 풀어나갈지 가늠이 되지 않는다.
# 모든 경로를 입력해서 최적의 경로가 나올때까지 돌리는 방법일 것 같은데...
# 일단 아무 경로를 돌린다. 최소비용이 나오면 함수에 입력한다. 다음 방법으로 넘어간다. 만약, 더 적은 비용이 나온다면 갱신한다.
# 근데, 합을 진행하다가 현재 있는 최소비용보다 커질수 있다.(결과가 나오기도 전에) 그러면 더이상 진행하지 않고 되돌아간다.(백트래킹)
# 개인적인 느낌은 무대뽀로 모든 수를 넣어보고 최솟값을 구하는데, 어느정도 최적화를 해야하니 백트래킹을 통해
# 어느 조건(여기선 현재까지 구한 최솟값)보다 크면 중단하고 되돌아가서 경로를 재탐색하는 것이다.
# 일단은 구현해보겠다.
import sys

def backtracking(path, cost):
    global min_cost
    
    # 모든 도시를 방문했을 경우
    if len(path) == N:
        start = path[0]  # 출발도시
        last_city = path[-1]  # 마지막 방문 도시(-1을 쓴 이유는 리스트의 마지막 요소를 가져오기 위해서)
        if W[last_city][start] > 0:  # 출발지로 돌아갈 수 있는 경우(출발지로 돌아간다는 조건에 맞는 경우)
        # 여기서 W[i][j]은 비용 행렬로 도시 i에서 j로 가는 비용으로 이해하면 된다.
        # W[i][j] = 0 이면 이동할 수 없고 W[i][j] > 0은 이동할 수 있다는 뜻이다.
            min_cost = min(min_cost, cost + W[last_city][start]) # 위의 값과 기존값과 비교해 최솟값으로 최소 비용 갱신
        return  # 결과를 돌려준다.
    
    # 백트래킹요소: 현재 비용이 최소 비용보다 크면 종료시키고 다른 경우를 찾는다.
    if cost >= min_cost:
        return
    
    # 밑의 코드는 도시의 거리를 지나가는 경우와 되돌아 오는 것을 제외하는 코드를 작성해야할 것 같다.
    
    # 다음 방문할 도시를 찾는다.
    for next_city in range(N):
        if next_city not in path and W[path[-1]][next_city] > 0:
        # 해당부분이 어려울수 있는데, 영어 시험본다 생각하자 not in path(방문하지 않았고)이고
        # W[path[-1]][next_city] > 0 는 이동가능하다는 뜻이다.
            path.append(next_city)  # 경로에 추가
            backtracking(path, cost + W[path[-2]][next_city])   # 재귀를 호출한다.
            # 이전 방문 도시를 의미하며, 현재 방문한 도시에서 다음 도시로 가는 비용을 더합니다.
            # 바로 윗줄에서 추가된 next_city가 현재 path[-1]이고 해당 도시 전에 추가된 것이 path[-2]이다
            path.pop()  # 백트래킹 (원래 상태 복귀), 있었던 도시(인자)를 뺍니다
            
            
# 입력 처리
N = int(input())  # 도시수
W = [list(map(int, input().split())) for _ in range(N)] # 비용 행렬
# N에 입력된 도시수만큼 도시별 비용을 입력 받겠다는 뜻이다.

min_cost = sys.maxsize  # 최소 비용을 초기화한다. 
# 만약에 해당 문구가 없다면 위의 min(min_cost, cost + W[last_city][start])에서 비교 대상이 없어 오류가 나온다.
# 그렇다고 min_cost = 0 을 하면 전 문제와 다르게 작은값을 구하므로 항상 답이 0이 나오는 경우가 발생된다.

# 시작은 모든 도시에서 가능
for start in range(N):
    backtracking([start], 0)   # 시작 도시만 포함한 경로로 시작
    
print(min_cost)  # 최소 비용 출력

# 해당 문제도 어렵다... GPT와 블로그들의 도움을 많이 받았다. 클론코딩 형식
# 솔직히 이해하는데 시간이 너무 오래 걸렸다. 아직까지도 입력된 여러 도시에서 최소비용을 구해야되서 백트래킹을 사용해야된다는건 알겠는데
# 왜 이렇게 나오는지는 2차원배열이 익숙치 않아서 그런것 같아 공부를 더해봐야겠다.
# 다른 문제를 위해 여기까지 하고 다음 문제로 넘어가겠다.
# 미련이 남아서 공부했는데, 해당 문제는 그림을 그려보니 단번에 이해가 갔다. 
# 입력값이 2차원 배열로 되어 있어서 이해가 안되는 것이었다. 만약 다음에도 이해가 안된다면, 인풋값을 인자로 두고 표를 그려보자.