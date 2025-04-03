from collections import deque

def BFS(start_node, end_node, graph):
    # 응용 포인트1: {노드: [경로]}
    queue = deque([start_node])
    visited = set([start_node])
    path = {start_node: [start_node]}

    while queue:
        curr_node = queue.popleft()

        # 응용 포인트2, 3: 최단경로의 길이를 통한 최단거리
        if curr_node == end_node:
            return path[curr_node], len(path[curr_node]) - 1

        for next_node in graph[curr_node]:
            if next_node not in visited:
                visited.add(next_node)
                queue.append(next_node)
                # 응용 포인트1: {다음노드: [현재경로] + [다음경로]}
                path[next_node] = path[curr_node] + [next_node]

    return [], -1

