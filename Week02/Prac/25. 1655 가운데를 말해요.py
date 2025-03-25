# 문제에 있는 글 그대로이다.
# 계속해서 정수를 입력할텐데 홀수면 중간값을 출력하면되고
# 만약 짝수값이라면 중간 두수중 작은 수를 출력하면된다.
# 문제는 이것을 힙정렬로 어떻게 구현하는가이다...

# 찾아보니 이 문제의 핵심은 left(중앙이하)와 right(중앙이상)를 나누어서 입력되는 값마다 번갈아가며 입력한다.
# left의 루트값보다 작으면 left 아니면 right에 저장
# 두 힙의 쿠기를 조절하여 중앙값을 유지합니다.
# left는 right보다 같거나 많아야합니다.(만약 left가 right보다 2개 이상 크면 left에서 하나 빼서 옯김)
# 그런데 left는 -로 저장하여 최댓값이 루트로 오게합니다.

import sys
import heapq

# 1. 두 개의 힙 초기화
left_heap = []  # 최대 힙 (중앙값 이하의 값들) → 파이썬은 최소 힙만 지원하므로 음수 저장
right_heap = []  # 최소 힙 (중앙값 이상의 값들)

# 2. 입력 받기
N = int(sys.stdin.readline().strip())

# 3. 입력값을 처리하며 중앙값 출력
for _ in range(N):
    num = int(sys.stdin.readline().strip())

    # 4. 최대 힙(left_heap)과 최소 힙(right_heap)에 번갈아 가며 삽입(균형 조절)
    if not left_heap or num <= -left_heap[0]:  
    # left힙이 비어있거나 num이 left힙의 루트값(최대값)보다 작거나 같다면
    # 최대 힙이 비어있거나, 현재 입력값이 최대 힙의 최대값 이하라면
        heapq.heappush(left_heap, -num)  # 최대 힙(left)에는 음수로 저장 (파이썬에서 최대 힙 구현)
    else:
        heapq.heappush(right_heap, num)  # 최소 힙(right)에는 그대로 저장

    # 5. 힙의 크기 조절 (최대 힙이 최소 힙보다 크거나 같아야 함)
    if len(left_heap) > len(right_heap) + 1:  
    # left힙의 길이가 right힙의 길이 +1 보다 크다면
        heapq.heappush(right_heap, -heapq.heappop(left_heap))  # left → right 이동
    elif len(left_heap) < len(right_heap):
    # left힙의 길이가 right힙의 길이보다 작다면
        heapq.heappush(left_heap, -heapq.heappop(right_heap))  # right → left 이동

    # 6. 중앙값 출력 (항상 left_heap의 루트가 중앙값)
    print(-left_heap[0])
    
# 결국 left힙의 루트(최댓값)은 항상 중앙값이 된다.
# 이러한 로직과 코드를 짤 생각하는게 대단한 것 같다. 내 머리가 안좋아서 그런가...
# 문제를 보고 코드를 구현할 수 있는 경지에 오를때까지 열심히 학습해보겠다.
# 