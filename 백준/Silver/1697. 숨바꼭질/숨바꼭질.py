from collections import deque
import sys

def bfs(N, K):

    queue = deque([N])
    while queue:
        x = queue.popleft()
        if x == K:
            return arr[x]
        for nx in (x-1, x+1, 2*x):
            if 0 <= nx <= 10**5 and not arr[nx]:
                queue.append(nx)
                arr[nx] = arr[x] + 1
    
N, K = map(int, sys.stdin.readline().split())
arr = [0]*(10**5 + 1)
print(bfs(N, K))