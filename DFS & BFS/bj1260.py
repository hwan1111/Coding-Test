#1260, DFS와 BFS

def DFS(graph, node, visited = None):
    if visited is None:
        visited = []

    visited.append(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            DFS(graph, neighbor, visited)

    return visited

from collections import deque

def BFS(graph, start_node, visited = None):
    if visited is None:
        visited = []

    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

    return visited

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in range(len(graph)):
    graph[i].sort()

DFS_answer = DFS(graph, v)
BFS_answer = BFS(graph, v)
for i in range(len(DFS_answer)):
    print(DFS_answer[i], end = " ")
print()
for i in range(len(BFS_answer)):
    print(BFS_answer[i], end = " ")