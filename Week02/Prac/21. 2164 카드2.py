# 큐로 주어진 N까지 쌓은 다음에 디큐를 시키고 다음 수를 디큐해서 다시 추가하면 한 싸이클이 되지 않을까 싶다.
# 싸이클은 popleft 2번, 마지막으로 버린 값 push 1번 해당 과정을 길이가 1 될때까지 반복하면 된다.
import sys
from collections import deque

N = int(sys.stdin.readline())
que = deque()

for i in range(N):      # 카드가 될 que를 1부터 N까지 추가
    que.append(int(i+1))    # 0을 포함해서 5를 넣으면 0~4이므로 각각 +1씩을 해서 1~5되게 맞춰주었다.
    
while len(que) > 1:   ### que의 길이가 N이라서 == 1로 하면 루프가 실행안된다고 한다.
    que.popleft()
    que.append(que.popleft())    # 두 번째 카드를 뒤로 보낸다.
    
print(que[0])   # 마지막으로 남은 카드 출력

# 큰 뼈대는 내가 만들었고 오류가 나서 GPT를 통해 수정하였다.
# 위에도 써놨으나 len(que) == 1로하면 N으로 인풋을 받아서 작동되지 않는 다는 사실을 깨달았다.