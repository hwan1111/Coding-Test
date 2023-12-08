#5014, 스타트링크
#입력이 백만..
#제한시간 1초 -> O(nlogn)
#visited = [0]이면, 만약 u, d가 0이라고 가정시 오류가 발생할 수 있음 -> visited[nextfloor]가 방문하지 않았지만 이미 방문처리가 됐음을 알 수 있음
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