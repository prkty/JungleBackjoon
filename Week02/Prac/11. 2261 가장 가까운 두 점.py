# 문제 원리는 간단하다. 그냥 좌표들 중 첫 째 줄에 가장 가까운 두 점의 거리의 제곱을 출력한다.
import sys

# 입력 처리
n = int(sys.stdin.readline().strip())
points = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

#   p1, p2 두 점 사이의 거리 제곱을 계산(거리 계산 함수)
def dist(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
    # x좌표끼리 마이너스해서 제곱, y좌표끼리 마이너스해서 제곱하고 더한다. 

def closest_pair(points):
    # 가장 가까운 두 점의 거리 제곱을 구하는 함수
    def solve(start, end):
        # 분할 정복 방식으로 최소 거리 구하기
        if end - start + 1 <= 3:  # 점이 3개 이하라면 브루트포스로 계산
            min_dist = float('inf')  # 양의 무한대로 설정
            for i in range(start, end):   # 시작지점부터 끝지점까지 확인
                for j in range(i + 1, end + 1):   # 1씩 더해서 확인
                    min_dist = min(min_dist, dist(points[i], points[j]))
                    # 가장 가까운 두점의 좌표를 구한다.
            return min_dist # 구해진 좌표를 돌려준다.

        # 중간 기준으로 분할
        mid = (start + end) // 2
        mid_x = points[mid][0]

        d = min(solve(start, mid), solve(mid + 1, end))  # 좌우 각각 최소 거리 구하기

        # x축 기준으로 d 이내에 있는 점들을 모아줌
        candidates = []
        for i in range(start, end + 1):
            if (points[i][0] - mid_x) ** 2 < d:
                candidates.append(points[i])  # x 축기준으로 d이내에 있는 점들을 카디날리티 리스트 추가

        # y축 기준 정렬(최소 거리 검사)
        candidates.sort(key = lambda p : p[1])

        # 스트립 내에서 최소 거리 계산
        len_c = len(candidates)
        for i in range(len_c - 1):
            for j in range(i + 1, len_c):
                if (candidates[j][1] - candidates[i][1]) ** 2 >= d:
                    break  # y좌표 차이가 d 이상이면 더 볼 필요 없음
                d = min(d, dist(candidates[i], candidates[j]))

        return d

    return solve(0, len(points) - 1)

# x좌표 기준으로 정렬
points.sort()

# 최소 거리 출력 (제곱근을 씌우지 않은 상태로 출력)
print(closest_pair(points))

# 반정도 이해했다. 오늘 어려운 문제 한바퀴 돌고, 개념, 북습하고 다시 확인해보겠다.
