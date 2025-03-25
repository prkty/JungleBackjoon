# 원래는 어려워보여서 다른문제를 풀다 다시왔다.
# 근데 생긴 코드와 달리 해석을 해보니 간단한 문제였다.
import sys

# 1. 입력 받기
data = sys.stdin.read().split()
M, N, L = map(int, data[:3])  # 사대 개수, 동물 개수, 사정거리 (인덱스 0~2까지)
shooters = sorted(map(int, data[3:M+3]))  # 사대 위치 재정렬(3부터 사대 수+2까지)
animals = list(zip(map(int, data[M+3::2]), map(int, data[M+4::2])))  # 동물 좌표(x,y)

# 2. 이진 탐색 함수 (가장 가까운 사대 찾기)
def can_hunt(x, y):
    left, right = 0, M - 1   # 0부터 시작이므로 실제 M값은 M-1까지이다.
    
    while left <= right:     # while 종료 조건문
        mid = (left + right) // 2  # 중앙값 (가까운 사대를 찾기 위한 이진 탐색)
        shooter = shooters[mid]   # 중앙값을 쓰기 편하게 변환
        
        # 사냥 조건 |x - a| + b ≤ L 확인
        # |x - a|는 사대와 동물의 가로 거리이다.
        # b는 동물의 세로 거리이다.
        # 합이 L(사정거리) 이하면 사냥 가능하다.
        # 이게 난 피타고라스로 풀어야하는줄 알았는데 좌표로 나타내므로 가로세로의 합으로 사정거리 적합도를 판단해도된다.
        if abs(shooter - x) + y <= L:
            return True  # 사정거리 이하이므로 사냥 가능 
        elif shooter < x:    # x가 사냥꾼보다 크면 
            left = mid + 1  # 더 오른쪽 탐색(동물이 오른쪽에 있으므로)
        else:   # 그외경우 x가 사냥꾼보다 작으면같은...
            right = mid - 1  # 더 왼쪽 탐색(동물이 왼쪽에 있으므로)

    return False  # 사냥 불가능(둘다 안되는 경우)

# 3. 동물 탐색 및 사냥 개수 계산
count = sum(1 for x, y in animals if can_hunt(x, y)) 
# 사냥되는 동물 좌표에 대해 can_hunt(x, y) = True이면 1을 부여

# 4. 결과 출력
print(count)

# 앞서말한것처럼 생각보다 쉬운 문제였다. 나는 어렵게 피타고라스의 정의써서 대각선을 구해야하는줄 알았는데,
# 팀원분께 여쭤보니, 좌표라서 그럴 필요가 없었다. 어디든 사정거리 값으로 비교하면된다.