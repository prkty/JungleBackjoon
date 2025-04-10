# 이 문제의 주의 점은 입력된 인풋이 등수이다. 문제 이해하는데 한참 걸렸다.
# 서류와 면접 둘 다에서 등수가 밀리면 뽑지 않는다
# 푸는 방식은 이러하다
# 서류 등수 기준으로 오름차순 정렬하여 성적이 좋은 순으로 나열
# 확인하여 현재까지 확인한 지원자들 중 면접 등수가 가장 높은 등수 기록
# 지원자 확인시, 해당 지원자의 면접 등수가 현재까지의 최고 면접 등수보다 높으면
# 해당 지원자는 선발 대상이고, 최고 등수로 갱신.
import sys
input = sys.stdin.readline

# 테스트 케이스의 수 입력
T = int(input().strip())

# 각 테스트 케이스에 대한 처리
for _ in range(T):
    # 지원자 수 입력
    N = int(input().strip())
    apply = []

    # 각 지원자의 서류 등수와 면접 등수 입력
    for _ in range(N):
        doc, interview = map(int, input().split())
        apply.append((doc, interview))

    # 서류 등수를 기준으로 오름차순 정렬(1부터)
    apply.sort()

    # 선발된 지원자 수 초기화
    selected_count = 0
    # 면접 등수의 최소값을 무한대로 초기화(비교를 위함)
    min_interview = float('inf')

    # 정렬된 지원자 리스트를 순회하며 선발 여부 결정
    for doc, interview in apply:
        # 현재 지원자의 면접 등수가 이전까지의 최소 면접 등수보다 높다면 선발
        if interview < min_interview:
            selected_count += 1
            min_interview = interview  # 최소 면접 등수 업데이트

    # 결과 출력
    print(selected_count)
# 문제가 이해되지 않아서 시간을 좀 쏟았다.
# 밑에 라인의 for문이 완벽히 이해되진 않지만(이게 어떻게 서류, 면접 순위를 고려하는지...)
# 시간 부족 관계로 다음 문제로 넘어가 보겠다.