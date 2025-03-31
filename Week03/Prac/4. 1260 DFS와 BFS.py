n, m, v = map(int, input().split())
matrix = [[0] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
  f, t = map(int, input().split())
  matrix[f][t] = matrix[t][f] = 1

def dfs(matrix, i, visited):
  stack=[i]
  while stack:
    value = stack.pop()
    if not visited[value]:
      print(value, end=' ')
      visited[value] = True
    for c in range(len(matrix[value])-1, -1, -1):
    # 문제에서 작은 숫자부터 입력하기를 요구해서 반대로 순회했습니다.
    # 순차적으로 하면 스택에 2,3,4 순으로 입력되고 4부터 pop되어
    # 가장 큰 수인 4부터 pop되기 때문입니다.
      if matrix[value][c] == 1 and not visited[c]:
        stack.append(c)

dfs(matrix, v, visited)

n, m, v = map(int, input().split())
matrix = [[0] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
  f, t = map(int, input().split())
  matrix[f][t] = matrix[t][f] = 1
  
from collections import deque

def bfs(matrix, i, visited):
  queue= deque()
  queue.append(i)
  while queue:
    value = queue.popleft()
    if not visited[value]:
      print(value, end=' ')
      visited[value] = True
      for c in range(len(matrix[value])):
        if matrix[value][c] == 1 and not visited[c]:
          queue.append(c)