# 해당문제는 히스토그램에서 높이가 같은 도표를 묶어서 제일 큰 넓이를 찾는 것이 목표이다.
# 스택을 쌓아서 같은 층인 값의 연속을 찾아서 높이와 너비를 곱해 찾으면 좀더 수월하다고 한다.
import sys

# 여러 줄 입력을 처리하기 위해 while 루프 사용
def largest_rectangle(hist):
    stack = []  # 스택이 들어갈 리스트 (막대의 인덱스를 저장)
    max_area = 0  # 최대 넓이 저장
    index = 0  # 현재 검사 중인 인덱스

    # 3. 모든 히스토그램 막대를 순회
    while index < len(hist):
        if not stack or hist[index] >= hist[stack[-1]]:
            stack.append(index)
            index += 1
        else:
            # 4. 스택에서 pop하여 넓이 계산
            top = stack.pop()
            height = hist[top]  # pop한 막대의 높이
            width = index if not stack else (index - stack[-1] - 1)
            max_area = max(max_area, height * width)

    # 5. 남은 요소 처리
    while stack:
        top = stack.pop()
        height = hist[top]
        width = index if not stack else (index - stack[-1] - 1)
        max_area = max(max_area, height * width)

    return max_area  # 최대 넓이 반환

# 6. 여러 개의 테스트 케이스 처리
while True:
    data = list(map(int, sys.stdin.readline().strip().split()))
    
    if data[0] == 0:  # 종료 조건 (첫 번째 값이 0이면 종료)
        break

    N = data[0]  # 히스토그램 개수
    histogram = data[1:]  # 히스토그램 높이 리스트
    
    print(largest_rectangle(histogram))  # 결과 출력