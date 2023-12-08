from collections import deque
import sys
def bfs(x, y, rainfall):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

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

for _ in range(N):
    terrain.append(list(map(int, sys.stdin.readline().split())))

result = 0

for rainfall in range(0, 101):
    visited = [[0] * N for _ in range(N)]
    count = 0

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and rainfall <= terrain[i][j]:
                bfs(i, j, rainfall)
                count += 1

    result = max(result, count)

print(result)