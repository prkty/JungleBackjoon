# 해당 문제는 N개의 정수로 이루어진 배열에 대해 앞의 수와 바로 뒷 수의 차가 제일 커야한다.
# 문제 이해도 잘안됐고, 코드 작성에 어려움이 있어 GPT와 블로그들의 도움을 받아 클론 코딩하며 이해했다.

from itertools import permutations   # itertools라는 라이브러리의 permutations 순열함수를 임포트해서 쓴다.

# 주어진 배열 arr에 대해 |A[i] - A[i+1]|의 합을 계산하는 함수이다.
def difference_sum(arr):
    total = 0    # 합을 저장할 변수의 초깃값을 0으로 한다.
    for i in range(len(arr) - 1):   # 전체 배열길이의 -1 만큼 반복(왜냐하면 조합이 N-1만큼 반복되므로)
        total += abs(arr[i] - arr[i + 1])   # 배열의 현재 인자와 다음 인자를 뺀걸 더한다. 
    return total   # 계산된 총 값을 돌려준다.

# 위에서 보낸 합을 토대로 차이의 합의 최대를 구하는 함수이다.
def difference_max(n, arr):  # 입력된 N만큼 반복한다.
    max_value = 0  # 최대 합을 저장할 변수의 초깃값을 0으로 한다.
    
    # 모두 가능한 순열을 생성하여 검사(매칭될 수 있는 모든 경우의 수를 고려한다고 생각하자)
    for perm in permutations(arr):   # permutations(반복가능한 객체, r)로 중복을 허용하지 않고 r개를 뽑아 나열한다. 그러나 뽑힌 순서는 생각한다.
        max_value = max(max_value, difference_sum(perm))  # 조합이 최대가 될때까지 최댓값을 갱신한다.
        # 현재의 합이랑 이후 계산한 새로 매칭된 조합의 합을 비교해서 더 큰것을 뽑기 위해 해당 코드를 쓴다.
        
    return max_value   # 최댓값을 반환한다. 들여쓰기 주의!
    
# 입력 처리
n = int(input())   # 첫번째줄의 배열의 갯수를 받는다.
arr = list(map(int, input().split()))    # 두번째줄의 배열 값을 받는다.

# 결과 출력
print(difference_max(n, arr))    # 최댓값을 프린트한다.

# 주석을 하나 하나 달고, 새로 임포트 하는 사이브러리인 itertools와 permutations함수에 대해 알아 보았다.
# permutations 라는 함수가 가능한 모든 수열을 생성한다는 것이 굉장히 편리한 것 같다.
# 코드에 주석을 달며 이해하긴 했으나 작성은 어려움을 느껴 다시 복습해야할 것 같다.