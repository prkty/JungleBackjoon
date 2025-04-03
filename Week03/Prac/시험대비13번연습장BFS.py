from collections import deque
import sys

input = sys.stdin.readline

def bfs(s_x,s_y,e_x,e_y):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    
    visited = set([(s_x, s_y)])
    
    queue = deque([(s_x, s_y, 1)])
    
    while queue:
        x, y, steps = queue.popleft()
        
        if x ==e_x and y==e_y:
            return steps
        
        for i in range(4):
            nx = x +dx[i]
            ny = y +dy[i]
            
            if 0 <=nx < N and 0 <= ny < M:
                if(nx, ny)not