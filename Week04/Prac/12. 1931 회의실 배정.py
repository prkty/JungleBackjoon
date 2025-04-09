# 여러개의 회의의 시작시간과 끝나는 시각이 있는데, 
# 이러한 회의의 수가 제일 많은 경우의 수를 출력하면된다.
# 푸는 아이디어가 도저히 생각나지 않아서 GPT를 참고했다.
# 종료 시간 기준으로 오름차순 정리하지만, 종료시간이 같으면 시작 시간 기준으로 정렬합니다.
# 가장 먼저 종료되는 회의를 기준으로 선택합니다. 
# 선택한 회의 종료 시간 이후에 시작하는 회의 중 가장 빨리 끝나는 회의를 선택하는 과정을 반복합니다.
# 수가 가장 크면 회의의 최대개수입니다.

import sys

input = sys.stdin.readline

# 회의수
N = int(input().strip())
meeting=[]

# 회의 시작, 종료 시각 저장
for _ in range(N):
    start, end = map(int, input().split())
    meeting.append((start, end))
    
# 회의 정렬: 종료 시간을 기준으로 오름차순, 종료 시간이 같으면 시작 시간을 기준으로 오름차순
def meeting_sort_key(m):
    return (m[1], m[0])  # 종료 시간 → 시작 시간 순으로 재정렬

meeting.sort(key = meeting_sort_key)

# 선택한 회의의 수
count = 0
# 마지막으로 선택한 회의의 종료 시간
last_end_time = 0

# 정렬된 회의들을 순회하며 회의 선택
for start, end in meeting:
    # 현재 회의의 시작 시간이 마지막 선택한 회의의 종료 시간 이후라면 선택
    if start >= last_end_time:
        last_end_time = end    # 마지막 회의 시간 갱신
        count += 1    # 회의 수 1 추가

# 최대 선택 가능한 회의의 수 출력
print(count)

# 회의수를 구하기 위해 머리로는 답을 아는데, 코드로 풀려면 어떻게 해야되는지
# 고민을 많이 했습니다. 그런데 생각보다 간단히 끝나는 시각 기준으로
# 다음 회의를 전개하여 최대수를 구한다는 사실이 특이했습니다.