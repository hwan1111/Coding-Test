#7569, 토마토

from collections import deque
import sys

def BFS():
    while queue:
        z, x, y = queue.popleft()

        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h:
                if box[nz][nx][ny] == 0:
                    box[nz][nx][ny] = box[z][x][y] + 1
                    queue.append((nz, nx, ny))

dx = [0, 0, 1, -1, 0, 0]
dy = [0, 0, 0, 0, 1, -1]
dz = [1, -1, 0, 0, 0, 0]
queue = deque()

m, n, h = map(int, sys.stdin.readline().split())

box = [[] for _ in range(h)]

for i in range(h):
    for j in range(n):
        box[i].append(list(map(int, sys.stdin.readline().split())))

for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                queue.append((i, j, k))

BFS()

cannotcomplete = False
day = 0

for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 0:
                cannotcomplete = True
            day = max(day, box[i][j][k])

if cannotcomplete:
    print(-1)
else:
    print(day - 1)