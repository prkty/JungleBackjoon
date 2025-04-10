import sys, heapq
input = sys.stdin.readline

N = int(input().strip())
room = []

for _ in range(N):
    num, start, end = map(int, input().split())
    room.append((num, start, end))
    
def rooms_sort(m):
    return(m[2],m[1],m[0])

room.sort(key = rooms_sort)

# for start, end in room:
#     if start >= last_end_time:
#         last_end_time = end  
#         count += 1   