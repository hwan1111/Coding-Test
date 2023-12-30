import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

visited = [[False for _ in range(M)] for _ in range(N)]
cnt = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def BFS(i, j, d):
    global cnt
    queue = deque()
    queue.append((i, j))
    visited[i][j] = 1
    cnt += 1

    while queue:
        x, y = queue.popleft()
        clean = 0

        for _ in range(4):
            d = (d + 3) % 4 
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                if visited[nx][ny] is False:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    cnt += 1
                    clean = 1   #반시계 방향으로 회전시 빈칸이 있다는 의미

                    break

        if clean == 0:  #청소할 곳이 없다면 후진
            if graph[x - dx[d]][y - dy[d]] != 1:
                queue.append((x - dx[d], y - dy[d]))
            else:
                print(cnt)
                break


BFS(r, c, d)