# 중요도가 큰것에서 작은순(내림차순)으로 문서를 정렬하고
# 큐에 대입하여 몇 번째인지 알아낸다.(중요도는 1 ~ 9)

import sys
from collections import deque

testcase = int(input())

for _ in range(testcase):
    N, M = map(int,sys.stdin.readline().strip().split())
    que = deque(enumerate(map(int, sys.stdin.readline().split()))) # 인덱스 자동 생성(중요도)
    
    count = 0  # 인쇄된 문서 개수(몇번째 문서인지)
    while que:
        # 현재 큐에서 가장 높은 중요도를 찾는다
        max_priority = max(priority for _, priority in que)
        # 맨 앞 문서의 중요도가 가장 높은지 확인(인덱스(순위)와 함께 써져있어 0괄호의 1번 숫자로 불러와야한다)
        if que[0][1] == max_priority:
            count += 1  # 중요도가 높다면 +1
            idx, _ = que.popleft()   # 그러고 왼쪽에서 하나를 뺀다.(인덱스랑)
            if idx == M:   # 찾던 문서 M이라면 출력한다.
                print(count)    # 해당 문서가 몇번째 문서인지 출력
                break
        else:
            que.append(que.popleft())   # 만약에 중요도가 높지 않으면 뽑아서 맨뒤로 이동한다.