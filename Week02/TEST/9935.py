# 첫째줄에 입력된 문자를 둘째 줄에 입력된 문자로 모두 지운다.
# 남으면 남은 문자 출력하고, 다지웠다면 FRULA이다
import sys

N = sys.stdin.readline().strip()  # 원본 문자열
M = sys.stdin.readline().strip()  # 폭발 문자열
stack = []

for i in N:
    stack.append(i)  # 현재 문자를 스택에 추가

    # 스택의 끝부분이 폭발 문자열과 같다면 제거(끝부분부터 검사)(도움)
    if stack[-len(M):] == list(M):
        for _ in range(len(M)):  
            stack.pop()  # 해당 열 하나씩 제거

# 결과 출력
if stack:
    print("".join(stack))  # 스택에 남은 문자열 출력(띄어쓰기 제거)
    # 이거 안쓰면 리스트 형식으로 뜨고 * 넣어도 띄어쓰기가 되므로 join을 통해 강제로 붙여준다.
else:
    print("FRULA")  # 스택이 비었다면 "FRULA" 출력