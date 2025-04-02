# 주어진 숫자들이 있으면, 주어진 기호들 사용 횟수에 따라 식을 세우고
# 그 결과값중 최솟값과 최댓값을 구하면된다.
# 해당 문제가 난이도가 있어 해결 방법을 찾아보았는데, dfs와 백트래킹을 사용해서
# 재귀적으로 반복하며 최솟값과 최댓값을 구하면 된다고 한다.
N = int(input())  # 수의 개수 N 입력

data = list(map(int, input().split()))   # 숫자들 입력

add, sub, mul, div = map(int, input().split())  # 연산자별 수 입력

# 최댓값과 최솟값 초기화(무한대로해서 비교를 하기 위함이다.)
max_value = -1e9
min_value = 1e9

# dfs로 모든 경우의 수 탐색
def dfs(i, arr):  # i는 현재 진행 중인 수열의 인덱스, arr은 주어진 수 배열
  global add, sub, mul, div, max_value, min_value  # 지역변수 호출
  # 주어진 수열을 다 받았을 경우 최댓값과 최솟값 계산
  if i == N:   # i가 수의 개수 N과 같으면
    max_value = max(max_value, arr)  # 기존 값이랑 현재 arr값중 더 큰것 반환
    min_value = min(min_value, arr)  # 기존 값이랑 현재 arr값중 더 작은것 반환
    return

  else:
    # 더하기
    if add > 0:  # 0보다 크다면 실행
      add -= 1  # 사용했으므로 대입해야되는 수 -1 후 실행
      dfs(i+1, arr + data[i])  # 현재 값에 i 더하고 다음(i+1)숫자 재귀
      add += 1   # 백트래킹을 위해 초기화 
    # 빼기
    if sub > 0:
      sub -= 1
      dfs(i+1, arr - data[i])
      sub += 1
    # 곱하기
    if mul > 0:
      mul -= 1
      dfs(i+1, arr * data[i])
      mul += 1
    # 나누기
    if div > 0:
      div -= 1
      dfs(i+1, int(arr / data[i]))
      div += 1
  
# DFS 메서드 호출
dfs(1, data[0])  
# 여기서 1은 인덱스인데, 0으로 쓰면 연산자가 부족해지고 불필요한 연산을 해야하는 문제가 생긴다.

# 최댓값과 최솟값 출력
print(int(max_value)) 
print(int(min_value))
# int 처리를 안해서 틀렸다고 나왔는데, 상단에서 최댓값 최솟값이 무한대로 비교하면서 float자료형이라서
# 오답 처리가 된거였다. int 처리를 꼭해주자.

# 문제 설명만 해석했을땐 코드를 어떻게 짜야할지 막막했는데,
# GPT를 통해 하나하나 살펴보니 어떤 로직으로 진행되고 백트래킹을 쓰는지 알게되었습니다.