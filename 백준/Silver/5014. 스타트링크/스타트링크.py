from collections import deque
import sys

def bfs(f, s, g, u, d):
    queue = deque([s])
    visited = [-1]*(f + 1)
    visited[s] = 0
    
    while queue:
        currentfloor = queue.popleft()

        if currentfloor == g:
            return visited[currentfloor]

        for nextfloor in (currentfloor + u, currentfloor - d):
            if 1 <= nextfloor <= f and visited[nextfloor] == -1:
                queue.append(nextfloor)
                visited[nextfloor] = visited[currentfloor] + 1
        
    
    return "use the stairs"

f, s, g, u, d = map(int, sys.stdin.readline().split())
print(bfs(f, s, g, u, d))