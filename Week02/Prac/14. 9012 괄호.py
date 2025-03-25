# 제대로 열리거나 닫힌 괄호는 VPS라고 하며 이번 문제는 VPS인지 아닌지 확인하는 문제이다.
# 해당문제는 스택을 통해 해결한다.
# 먼저 스택으로 여는 괄호를 push한다. 그리고 닫는 괄호를 확인되면 여는 괄호를 그만큼 pop한다.

import sys

# 1. 올바른 괄호 문자열(VPS) 판별 함수
def is_vps(string):
    stack = []  # 스택 선언

# for문을 통해 여는 괄호와 닫는 괄호의 수를 비교한다.
    for char in string:
        if char == "(":  # 여는 괄호이면 push
            stack.append("(")
            
        else:  # 닫는 괄호이면 스택의 여는 괄호를 pop 수행
            if not stack:  # 닫는 괄호가 더 많다면 NO 리턴(스택에 뺄게 없음)
                return "NO"
            stack.pop()  # 정상적인 경우 스택에서 '(' 제거

    return "YES" if not stack else "NO"  # 스택이 비어있으면 YES, 아니면 NO(닫는 괄호가 많았다면)

# 2. 입력 받기
N = int(sys.stdin.readline().strip())  # 테스트 케이스 개수

# 3. 여러 개의 테스트 케이스 실행 N 줄만큼 실행
for _ in range(N):
    string = sys.stdin.readline().strip()
    print(is_vps(string))
    
# 인터넷을 보니까 엄청 다양한 방법이 있다. 하나하나 빼서 새는법, 짝을 찾아서 빼면서 True/False 등
# 다양한 방법이 있는데, 나는 GPT가 추천한 스택에 넣어서 계산하는 것이 이 문제의 의도와 비슷하다고 생각되어
# 적합하다고 생각한다. 스택에 여는 괄호 넣고 닫는 괄호만큼 빼는 이론이 신박한 것 같다.