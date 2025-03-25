# 이거는 스택과 다르게 큐를 구현하는 것이다.
# 명령어를 통해 구현하면 되겠다. 
# 그러나 여기서는 일반 리스트로 구현하면 시간초과가 나오므로 from collections import deque를 사용한다.

import sys
from collections import deque

N = int(sys.stdin.readline())
que = deque()

for _ in range(N):  # 여기가 문제였다...
    cmd = sys.stdin.readline().split()
    
    if cmd[0] == "push":
        que.append(int(cmd[1]))
        
    elif cmd[0] == "pop":
        print(que.popleft() if que else -1)
        
    elif cmd[0] == "size":
        print(len(que))
        
    elif cmd[0] == "empty":
        print(1 if not que else 0)
        
    elif cmd[0] == "front":
        print(que[0] if que else -1)
        
    elif cmd[0] == "back":
        print(que[-1] if que else -1)
        
# 구현하고 나서 타입에러가 나서 당황했다. gpt에 물어보니 단순한 소괄호를 대괄호로 써서 나온 오류였다.