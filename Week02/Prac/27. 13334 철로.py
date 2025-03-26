import sys
import heapq

# 입력 받기
n = int(sys.stdin.readline().strip())
lines = []

# 주어진 n개의 직장-집 좌표 입력 받기
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    start, end = sorted([a, b])  # 항상 작은 값이 시작점이 되도록 정렬
    lines.append((start, end))

# 철로 길이 d 입력
d = int(sys.stdin.readline().strip())

# 1. 끝점을 기준으로 정렬 (끝점이 같다면 시작점이 작은 순)
lines.sort(key=lambda x: x[1])

# 2. 최소 힙을 활용한 탐색
heap = []
max_count = 0

for start, end in lines:
    # 현재 끝점(end)에서 d 이내에 포함되지 않는 시작점들을 제거
    while heap and heap[0] < end - d:
        heapq.heappop(heap)

    # 현재 시작점을 힙에 추가
    heapq.heappush(heap, start)

    # 힙의 크기가 현재 철로 내에서 포함되는 구간의 수
    max_count = max(max_count, len(heap))

# 최대 포함 개수 출력
print(max_count)
