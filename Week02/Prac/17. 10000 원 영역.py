import sys

# ✅ 1. 입력 받기
N = int(sys.stdin.readline().strip())
events = []

# ✅ 2. 원의 시작점과 끝점을 events 리스트에 저장
for _ in range(N):
    x, r = map(int, sys.stdin.readline().split())
    events.append((x - r, 1))  # 원의 시작점
    events.append((x + r, -1))  # 원의 끝점

# ✅ 3. x 좌표 기준 정렬 (같은 좌표라면 끝(-1)이 먼저)
events.sort(key=lambda e: (e[0], -e[1]))

# ✅ 4. 스택을 이용한 독립적인 영역 계산
stack = []
area_count = 1  # 최소 하나의 영역은 존재

for x, event_type in events:
    if event_type == 1:  # 원이 시작됨 (열림)
        if stack:  # 스택이 비어있지 않다면 기존 원 위에 새로운 원 추가됨
            area_count += 1
        stack.append(x)  # 시작점을 스택에 push
    else:  # 원이 끝남 (닫힘)
        stack.pop()  # 스택에서 원을 제거
        if stack:  # 스택이 비어있지 않다면 중첩된 원이 끝났으므로 새로운 영역 추가
            area_count += 1

# ✅ 5. 결과 출력
print(area_count)
