# 요세푸스 문제는 N명의 사람들이 K번째 사람이 될때마다 제거하는 것이다.
# 제거된 사람의 인덱스를 순서대로 출력만 하면 끝이다.
# 확인을 해보니 rotate를 통해 리스트를 회전해서 빼는 방식이 좋다.
import sys
from collections import deque

# 1. 입력 받기
N, K = map(int, sys.stdin.readline().strip().split())
queue = deque(range(1, N + 1))  # 1부터 N까지 큐에 저장(0제외하고 입력)
result = []  # 제거된 순서를 저장할 리스트

# 2. 요세푸스 순열 생성
while queue:       ### queue 리스트에 아무것도 남지 않을때까지 순환한다.
    queue.rotate(-(K-1))  # K-1번 앞 요소를 뒤로 이동 (K번째 사람이 맨 앞에 오게)
    # 예를 들어 K가 3이면 로테이션 -2가 되어서 3이 첫번째로 이동된다.
    result.append(queue.popleft())  # K번째 사람 제거
    # 로테이션되어서 3번이 맨앞에 있으므로 제거한다.

# 3. 출력 형식에 맞게 출력
print("<" + ", ".join(map(str, result)) + ">")   # '구분자'.join을 통해 숫자 사이 콤마를 넣을수 있다.
# 맨첨엔 3번째 인덱스를 빼고 리스트를 새로 만들어서 3을 빼야되나... 어떻게 요세푸스를 코드로 구현하나 고민을
# 했는데, rotate함수를 통해 빼야되는 수를 앞으로 당겨서 큐의 popleft에 따라 K번째를 뺄 수 있음을 알았습니다.
# rotate함수와 while 리스트: 로 리스트에 요소가 없을때까지 반복할 수 있음을 나중에 써먹어야겠습니다.
