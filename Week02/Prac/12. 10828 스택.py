# 그냥 스택을 구현하라는거랑 다름이 없다.
# 난 간단할 줄 알았는데, 생각보다 어려웠다.
# 명령어를 리스트 형식으로 인식해서 명령어를 나누는 생각이 주 핵심인 것 같다.
# 또한 파이썬은 스택이 따로 없으므로 리스트로 구현할 수 있다.
import sys

N = int(sys.stdin.readline())
stack = []

for _ in range(N):
    cmd = sys.stdin.readline().strip().split()   # 명령어를 받음
    
    if cmd[0] == "push":         # cmd받은 명령어의 0번째 요소가 push일시
        stack.append(int(cmd[1]))   # 정수 X를 스택에 push 
    
    elif cmd[0] == "pop":
        print(stack.pop() if stack else -1)   # pop으로 스택의 정수를 뺀다.(없으면 -1을 한다)
        # 파이썬은 음수 인덱싱을 지원하기 때문이다.
        
    elif cmd[0] == "size":
        print(len(stack))      # 스택의 길이를 출력합니다.
    
    elif cmd[0] == "empty":
        print(1 if not stack else 0)          # 스택에 없으면 1 있으면 0 출력
    #    print(1 if stack != 0 else 0)   이렇게 쓰면 리스트는 0과 비교할 수 없어, 항상 참이라서 쓸수 없다고한다.
    
        
    elif cmd[0] == "top":
        print(stack[-1] if stack else -1)    # 최근 넣은 값을 보여주고 없으면 -1