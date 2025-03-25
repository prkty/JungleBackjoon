# 두 묶음 카드 A, B를 하나로 만들기 위해 만들어지는 경우의 수를 구합니다.
# 3묶음의 A,B,C(최솟값순으로 정렬된)가 있다면 (A+B)+((A+B)+C)일 때의 값이 최소 비교 횟수를 출력합니다.
# 솔직히 문제 이론이 어렵습니다.
# 최소 비교 횟수를 출력하려면 더해지는 두개의 카드 값은 3개의 카드값중에 제일 작은 두개여야합니다.
# N이 얼마냐에 따라 묶어야되는 카드 묶음수가 늘어나므로 힙 정렬로 최솟값을 찾아야합니다.
import sys
import heapq

# 1. 입력 받기
N = int(sys.stdin.readline().strip())
heap = []

for _ in range(N):
    heapq.heappush(heap, int(sys.stdin.readline().strip()))  # 카드 묶음 최소 힙에 삽입

# 2. 최소 비교 횟수 계산(초기값은 0)
total_comparisons = 0

while len(heap) > 1:   # 묶음이 1이상일때까지 실행(즉, 카드가 하나로 합쳐질 때까지 실행)
    # 3. 가장 작은 두 묶음을 꺼내어 합침
    first = heapq.heappop(heap)  # 첫 최솟값을 꺼낸다
    second = heapq.heappop(heap) # 두번째 최솟값을 꺼낸다
    sum_cards = first + second  # 현재 묶음의 비교 횟수

    total_comparisons += sum_cards  # 총 비교 횟수 누적
    heapq.heappush(heap, sum_cards)  # 합친 카드 묶음을 다시 힙에 넣음

# 4. 결과 출력
print(total_comparisons)   # 최종 비교 횟수 총합 출력

# 해당 문제는 문제 설명도 이해하기 어려워서 다른 동료의 설명을 듣고 이해했다.
# 이 문제의 핵심은 최소 비교 횟수를 출력하기 위해 힙정렬을 통해
# 첫번째와 두번째의 최솟값을 추출해서 더한다는 사실이다.
# 해당 과정을 묶음이 1이될 때까지 하면된다.
