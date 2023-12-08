#2468, 안전영역

from collections import deque
import sys

def bfs(x, y, rainfall):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if rainfall <= terrain[nx][ny] and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1

N = int(sys.stdin.readline())

terrain = []

for i in range(N):
    terrain.append(list(map(int, sys.stdin.readline().split())))

highest = max(terrain[i][j] for i in range(N) for j in range(N))
lowest = min(terrain[i][j] for i in range(N) for j in range(N))

result = 0

for rainfall in range(lowest-1, highest+2):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if rainfall <= terrain[i][j] and not visited[i][j]:
                bfs(i, j, rainfall)
                cnt += 1

    result = max(result, cnt)

print(result)