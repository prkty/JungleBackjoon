# 문제의 예시도 그렇고 친절하지 않은 문제인 것 같다.
# x축위에 원을 N개 그릴 수 있고, 교차하는 경우는 없지만 접할 수는 있다고 한다.
# 주어진 x좌표와 r(반지름)에 따라 원을 그릴 수 있고 바깥부분도 세어야한다.
# 예를 들어 큰 원안에 작은원 둘이 접하면 영역은 2개가 된다.
# 문제에 예시로 보여준 그림은 6가지이다.
# 그러면 원이 접하는 경우 영역의 갯수를 2로 올리고, 접하지 않으면 1로 올리는 코드를 작성해야한다.

import sys

# 1. 입력 받기
N = int(sys.stdin.readline().strip())
events = []

# 2. 원의 시작점과 끝점을 events 리스트에 저장(입력은 원의 중앙값과 반지름을 입력하므로)
for _ in range(N):
    x, r = map(int, sys.stdin.readline().split())
    events.append((x - r, 1, x))  # 원의 시작점(x - r), 시작점을 의미하는 1, x좌표
    events.append((x + r, -1, x))  # 원의 끝점(x + r), 끝점을 의미하는 -1, x좌표

# 3. x 좌표 기준 정렬 (같은 좌표라면 끝(-1)이 먼저)
events.sort(key = lambda e: (e[0], -e[1]))
# 람다를 정렬 기준으로 삼는 이유는 간단한 정렬 기준을 설정하기 위해서이다.
# def 정렬함수로 하면 길어지기 때문이다.
# 끝점은 -1로 처리되어 있기 때문에 올바른 순서로 좌표를 지정하기 위해 끝점에 -1처리를 하여 순서대로 x좌표 정렬이 되게끔한다.
# (안그러면 x좌표가 꼬인다)

# 4. 스택을 이용한 독립적인 영역 계산
stack = []
area_count = 1  # 최소 하나의 영역은 존재(바깥)

# 원의 시작점(1)이 나오면 스택에 올린다
# 원의 끝점(-1)이 나오면 스택에서 뺀다
# 새로운 원이 시작시, 기존 원과 겹치면 +1
# 원 하나가 끝나도 중첩된 원이 존재하면 +1
# 더나아가서 내부적으로 포함된 원은 +2가 될 것이다.
# 여기 코드를 할 때 주로 생각해야하는 건 접하면 +1이라는 것이다.
# 다음 원을 비교하더라도 시작점엔 이미 빼진 원이기 때문에 종료지점만 접하는지 판단해서 +1을 한다. 
for x, event_type, center in events:   # 여기서 event_type은 1이면 시작점, -1이면 끝점을 의미한다.
    if event_type == 1:  # 원이 시작됨 (1 열림)
        if stack:  # 스택이 비어있지 않다면, 기존 원 위에 새로운 원 추가됨
            area_count += 1   # 영역 +1
            
            # 스택의 최상단 원의 중심과 현재 원의 중심이 다르면 내부적으로 포함된 원 (접하는 것이 아닌 완전히 포함)
            if stack[-1] != center:
                area_count += 1  # 내부에 포함된 경우 +1
                
        stack.append(center)  # 시작점을 스택에 push
        
    else:  # 원이 끝남 (-1 닫힘)
        stack.pop()  # 스택에서 원을 제거
        if stack:  # 스택이 비어있지 않다면, 중첩된 원이 끝났으므로 새로운 영역 추가
            area_count += 1    # 영역 +1

# 5. 결과 출력
print(area_count)

# 문제 해석도 주어진 정보가 적고 제대로 안적혀있어서 이해하는데 시간을 좀 썻다.
# 코드 구현도 스택을 합쳐서 구현해서 시간이 좀 걸렸는데, 몇줄 코드 이해하는데 한시간 걸린 것 같다.
# 이문제는 시작점과 끝점을 분리해서 순서대로 정렬하고 스택을 통해 접하는 지점을 찾으며 찾으면 구역을 +1을 한다.
# 특히나 밑의 for문이 이해하는데 시간이 오래걸렷고 다시 이문제를 만난다면 단번에 이해하기는 어려울 것 같다.
# 다음에 만난다면 직접 그리면서 이해하고 코드를 작성해보겠다.



# 원이 들어오는 모양을 괄호로 변환하여 공간 계산
import sys

input = sys.stdin.readline

n = int(input())
circles = []

# 원의 왼쪽은 '(' 모양의 괄호 오른쪽은 ')' 모양의 괄호로 만든다.
for i in range(n):
  x, r = map(int, input().split())
  circles.append((x-r, '('))
  circles.append((x+r, ')'))

# 좌표기준으로 오름 차순으로 정렬하되 좌표가 같으면 ')'모양이 앞에 오게 정렬한다.
circles = sorted(circles, key= lambda x:(x[0], -ord(x[1])))

stack = []
# 스택에는 좌표, 괄호 모양, 상태값이 들어감
answer = 1
for i in range(n*2):
  position, bracket = circles[i]
  if len(stack) == 0:
    stack.append({'pos':position,'bracket':bracket,'status':0})
    continue
  
  # status 0: 기본값 ->
  # status 1: 원 안의 원이 연결 되어 있는 지 확인
  # 괄호가 닫히면 status 값을 확인하고 0 이면 +1 1이면 +2
  if bracket == ')':
    if stack[-1]['status'] == 0:
      answer +=1
    elif stack[-1]['status'] == 1:
      answer +=2
    stack.pop()
    # 원이 이어져 있는지 확인
    if i != n*2-1:
      if circles[i+1][0] != position:
        stack[-1]['status'] = 0
  else:
    if stack[-1]['pos'] == position:
      # 좌표값이 같으면 원이 접해있는 상태
      stack[-1]['status'] = 1
      stack.append({'pos':position,'bracket':bracket,'status':0})
    else:
      # 좌표값이 같지 않으면 원이접하지 않음
      stack.append({'pos':position,'bracket':bracket,'status':0})

print(answer)