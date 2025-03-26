# 올바른 괄호열을 찾고 고라호열의 값을 찾는 것이 목적이다.
# 그러나 괄호열이 맞지 않는 다면 0으로 출력한다.
# ()는 *2이고 []는 *3 인데, 문제만 보고는 이해하기 힘드니,
# 입력과 출력을 비교하면서 이해하는 것이 좋다. 
# 왜냐하면, 괄호의 위치에 따라 곱하는지 더하는지가 다르다.

# 스택을 활용하여 여는 괄호를 만나면 스택에 push하고 닫는 괄호면 올바른 구조인지 확인하고 계산합니다.
# 형식이 앞의 괄호문제와 유사합니다.
# ()와 []를 겹치면 판단할 수 없으니 스택에 쌓아서 짝을 찾는 것이다.


import sys

# 입력단
UVPS = sys.stdin.readline().strip()

def cal_UVPS_value(UVPS):
    stack = []
    temp = 1
    result = 0
    
    for i in range(len(UVPS)):
        char = UVPS[i]
        
        if char == '(':
            stack.append(char)
            temp *= 2     # ()는 2를 곱한다.
            
        elif char == '[':
            stack.append(char)
            temp *= 3    # []는 3을 곱한다.
            
        elif char == ')':
            if not stack or stack[-1] != '(':  # 스택이 비어있지 않거나 최근 값이 (이 아닌경우
                return 0   # 아무것도 리턴하지 않음
            if UVPS[i-1] == '(':   # 즉시 계산 가능시 추가
                result += temp    # 현재의 temp값을 더합니다.
            stack.pop()    # (를 제거합니다.
            temp //= 2   # 닫힌 괄호가 나왔으므로 2로 나눕니다.(원상태 복구)
            
        elif char == ']':
            if not stack or stack[-1] != '[':  # 스택이 비어있지 않거나 최근 값이 [이 아닌경우
                return 0
            if UVPS[i-1] == '[':  # 즉시 계산할 수 있는 `[]` 패턴
                result += temp  # 현재 temp 값을 추가
            stack.pop()  # [를 제거합니다
            temp //= 3  # 닫힌 괄호가 나왔으므로 3으로 나눈다.
            
        # 모든 연산이 끝났을 때 스택이 비어있어야 함 (올바른 괄호 문자열인지 체크)
    if stack:
        return 0

    return result
            
            
print(cal_UVPS_value(UVPS))

# 해당 공식은 작동 방식이 신기하다. 그런데 답은 맞다.
# (()[[]])를 예시로 설명하겠다.
# 1. 여는 소괄호로 temp = 2
# 2. 여는 소괄호로 temp = 4, result = 0
# 3. 닫는 소괄호로 temp = 4 // 2 = 2, result = 4
# 4. 여는 대괄호로 temp = 6
# 5. 여는 대괄호로 temp = 18
# 6. 닫는 대괄호로 temp = 18 // 3 = 6, result = 4 + 18 = 22
# 7. 닫는 대괄호지만, 스택 = ['(']이므로 temp = 6 // 3 = 2, result = 22
# 8. 닫는 소괄호고 스택도 없지만, 최근값이 (이 아니므로 return 0으로 결과에 반영이 안됨
# 결과는 22이다.
# 이론은 직접해보니 이해하기 쉬웠는데, 코드로는 좀 복잡해서 코드를 이해하는데 시간이 좀 걸렸다.