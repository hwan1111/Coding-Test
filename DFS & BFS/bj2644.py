#2644, 촌수계산

from collections import deque
import sys

def bfs(start, end):
    visited = [False]*(N+1)
    queue = deque([start])
    visited[start] = 1

    while queue:
        current = queue.popleft()
        if current == end:
            return visited[current]-1
        for next in graph[current]:
            if not visited[next]:
                queue.append(next)
                visited[next] = visited[current] + 1

    return -1

N = int(sys.stdin.readline())
v1, v2 = map(int, sys.stdin.readline().split())
M = int(sys.stdin.readline())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

print(bfs(v1, v2))