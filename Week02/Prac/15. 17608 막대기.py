# 보는 방향에서 봤을때 보이는 막대의 갯수를 구하는 문제이다.
# 스택으로 쌓아서 마지막 부분부터 스캔하면서 제일 막대보다 큰것을 업데이트하면서
# 기존값보다 큰값이 있으면 갯수를 한개씩 올리면 되지 않을까싶다.

import sys
sysinput = sys.stdin.readline

# 인풋값
N = int(sysinput())
stack = []


for _ in range(N):         # N만큼 스택에 막대 높이를 추가합니다.
    stack.append(int(sysinput()))
    
last =  stack[-1]    # 스택에서 마지막 값
count = 1       # 뒷 첫 블럭은 무조건 보이므로 미리 1을 넣어줌

for i in reversed(range(N)):    # N줄 범위를 stack i의 역으로 확인한다.(하나씩 비교)
    if stack[i] > last:         # 직전막대보다 새로 비교하는 값이 크다면
        count += 1              # 카운트를 1올린다
        last = stack[i]         # 전 막대보다 크므로 비교할 값으로 업데이트한다.
        
print(count)

# 이론은 이해됐는데, 코드로 어떻게 구현할지 몰랐다. 근데, 완성된 코드를 보니 이해가 된다.
# 스택쌓은걸 역으로 확인하면서 큰값을 업데이트하며 비교하는 것이 중요한 포인트 같다.