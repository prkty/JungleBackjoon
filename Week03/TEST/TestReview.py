from collections import deque

bfs_q = deque()
danji = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]

n =  int(input())
for _ in range(n):
    danji.append(list(map(int, input())))


#단지 구분
def bfs_danji(danji):
    bfs_q.append((0, 0))

    while bfs_q:
        x, y = bfs_q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                danji[nx][ny] = 2
                bfs_q.append((nx, ny))  



#집 수 카운트 성공
def bfs_home(danji):
    bfs_q.append((0, 0))
    count = 0

    while bfs_q:
        x, y = bfs_q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and danji[nx][ny] == 1:
                danji[nx][ny] = 2
                bfs_q.append((nx, ny))  
                count += 1



bfs_danji(danji)