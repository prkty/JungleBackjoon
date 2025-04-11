import sys
import heapq

input = sys.stdin.readline

n = int(input())
lectures = []

for _ in range(n):
    num, start, end = map(int, input().split())
    lectures.append((start, end, num))

# 시작 시간 기준으로 정렬, 시작 시간이 같으면 종료 시간 기준으로 정렬
lectures.sort(key=lambda x: (x[0], x[1]))

# 우선순위 큐: (강의 종료 시간, 강의실 번호)
pq = []
# 강의실 번호 할당을 위한 변수
room_number = 0
# 각 강의에 배정된 강의실 번호를 저장할 딕셔너리
lecture_room = {}

for start, end, num in lectures:
    # 현재 강의의 시작 시간보다 작거나 같은 종료 시간을 가진 강의실이 있다면 재사용
    if pq and pq[0][0] <= start:
        _, room = heapq.heappop(pq)
    else:
        # 새로운 강의실 필요
        room_number += 1
        room = room_number
    # 현재 강의의 종료 시간과 배정된 강의실 번호를 우선순위 큐에 추가
    heapq.heappush(pq, (end, room))
    # 해당 강의 번호에 배정된 강의실 번호 저장
    lecture_room[num] = room

# 최소 강의실 개수 출력
print(room_number)
# 각 강의 번호에 해당하는 강의실 번호 출력
for i in range(1, n + 1):
    print(lecture_room[i])