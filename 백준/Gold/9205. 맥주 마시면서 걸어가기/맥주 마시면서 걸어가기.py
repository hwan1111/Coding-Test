from collections import deque
import sys

def BFS():
    queue = deque()
    queue.append((home_x, home_y))

    while queue:
        x, y = queue.popleft()

        if abs(x - rock_x) + abs(y - rock_y) <= 1000:
            print('happy')
            return
        for i in range(n):
            if visited[i] is False:
                nx, ny = convinience[i]
                if abs(x - nx) + abs(y - ny) <= 1000:
                    visited[i] = True
                    queue.append((nx, ny))
    print('sad')
    return

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    visited = [False for _ in range(n+1)]
    home_x, home_y = map(int, sys.stdin.readline().rstrip().split())
    convinience = []
    for i in range(n):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        convinience.append((x, y))
    rock_x, rock_y = map(int, sys.stdin.readline().rstrip().split())

    BFS()