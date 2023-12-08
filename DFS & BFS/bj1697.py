#1697, 숨바꼭질
#시간 제한 -> 2초 -> 10^16
#입력 수 2*10^5 -> O(n^3) 저질 코드 ok
#(수빈이 좌표: N, 동생 좌표: K)
#걷는다면 +- 1, 순간이동 한다면 *2
#수빈이가 동생을 찾을 수 있는 가장 빠른 시간

from collections import deque
import sys


def bfs(N, K, visited=[0]*(10**5 + 1)):
    queue = deque([N])

    while queue:
        x = queue.popleft()
        if x == K:
            return visited[x]
        for nx in (x-1, x+1, 2*x):
            if 0 <= nx <= 10**5 and not visited[nx]:
                queue.append(nx)
                visited[nx] = visited[x] + 1

N, K = map(int, sys.stdin.readline().split())

print(bfs(N, K))