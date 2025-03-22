# 먼저 그림을 그려보면 문제를 이해하는건 어렵지 않다.
# 일단 내가 아는 건 N은 나무 갯수이고 M은 집에 가져가야하는 나무 길이
# H는 결과로 알아야되는 절단기 최댓값이라는 점이다.
# 나무 N개의 길이를 받을 수 있는 Tree_length도 받아야한다.
import sys

N, M = map(int, sys.stdin.readline().split())
Tree_length = list(map(int, sys.stdin.readline().split()))
# high = 절단기 결과

# 이분탐색을 하려면 자를 높이의 최솟값(0)과 최대값(가장 긴 나무)를 설정해야한다.
low, high = 0, max(Tree_length)

# 이분 탐색을 시작한다. 계속해서 반복하면 절단하는 나무 M을 가져가기 위한 최댓값을 출력 할 수 있다.
while low <= high:    # 기존의 pl과 pr이라 생각하면 편하다. 조건값을 찾으면 종료한다.
    mid = (low + high) // 2    # 중간값을 정한다.
    
    # 우린 잘린 나무의 합이 M보다 크기만 하면 된다.
    # mid 높이에서 잘랐을 때 가져올 수 있는 나무 총량을 계산한다.
    wood = sum(tree - mid for tree in Tree_length if tree > mid) 
    # 위의 리스트 컴프리헨션을 풀어보면 밑에 공식과 같다.
    # wood = 0  # 가져올 수 있는 나무의 총량이다.
    # for tree in Tree_length:     # 트리 리스트에 있는 트리들의 높이들을 하나씩 수행해 본다.
    #     if tree > mid:   # 나무가 자르는 높이(mid)보다 클 때만 계산(제일 큰 나무가 기준이라 작을 때는 없다)
    #         wood = wood + (tree - mid)  # 기존 나무에서 잘린 부분만 합산.
            
    if wood >= M:    # M보다 더 많이 짤렸을때 기준값에 최솟값을 1 올린다.
        low = mid + 1
    else:            # 그 외의 경우(M보다 클때)는 기준값에 높이 최댓값을 1 내린다.
        high = mid - 1
                
                
# 절단기의 높이를 출력한다.
print(high)

# 두번재 문제인데도 벌써 어렵다. GPT의 도움을 받아 작성했다.
# 잠을 많이 못자 컨디션이 좋지 않은지 이해가 잘 되지 않는다... 