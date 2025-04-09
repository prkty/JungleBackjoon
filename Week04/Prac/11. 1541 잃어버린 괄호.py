# 주어진 입력에 대해 적절한 괄호로 최솟값을 만드는 것이다.
# 이러한 최솟값을 구하려면 -바로 다음에 괄호를 치면 된다. 그래야 빼지는 수가 커지니까
# 기호별로 나누어서 -나오면 괄호 붙이고, 맨마지막에 닫는 괄호 붙여서 계산하려 했다.
import re


n = input()
n = re.findall(r'\d+|[+-]', n)   # 숫자, 기호별로 분해 
# (\d: 하나이상의 숫자, |: 또는, re.findeall(): 정규표현식에 맞는 모든 항목을 순서대로 리스트로 추출)

i = 0
while i < len(n):
    if n[i] == '-':
        n.insert(i + 1, '(')  # - 다음 위치에 ( 삽입
        i += 1  # 새로 들어간 '(' 건너뛰기
    i += 1
else:
    n.append(')')
print(n)

# 계산 어케함? 닫는 괄호 위치도 이상함 ㅋㅋ


############################################################

# 내 아이디어를 수정한게 밑에 수식이다.
import re

n = input()
tokens = re.findall(r'\d+|[+-]', n)

result = 0
temp = 0
minus_found = False

i = 0
while i < len(tokens):
    token = tokens[i]

    if token == '+':
        i += 1
        continue
    elif token == '-':
        minus_found = True
        i += 1
        continue

    num = int(token)

    if not minus_found:
        result += num
    else:
        # 뺄셈 이후엔 모든 수를 한꺼번에 빼기
        temp += num
        # 다음 기호가 '+'이면 계속 더함
        if i + 1 >= len(tokens) or tokens[i + 1] == '-':
            result -= temp
            temp = 0

    i += 1

print(result)

############################################################

# -를 기준으로 앞에 내용끼리 더하고 뒤에 내용 더해서 빼는 방식이다. 
# 수식 입력 받기
expr = input()

# '-'를 기준으로 나누기 → 가장 중요한 핵심!
parts = expr.split('-')

# 첫 번째 덩어리는 괄호 없이 그냥 더함
first = sum(map(int, parts[0].split('+')))

# 두 번째 이후 덩어리는 +로 나눈 뒤 모두 더해서 한꺼번에 뺌
rest = 0
for part in parts[1:]:
    rest += sum(map(int, part.split('+')))

# 결과 출력: 첫 덩어리에서 나머지를 한 번에 빼기
print(first - rest)
# 내 방식으로 풀어보려다 무리가 있었다.
#그래서 - 기준으로 나누어서 계산하는 방식으로 수정했다.