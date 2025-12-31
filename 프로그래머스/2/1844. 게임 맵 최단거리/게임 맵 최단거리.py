from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    # 이동 방향 (상, 하, 좌, 우)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    # 거리 정보를 저장할 리스트 (방문하지 않은 곳은 -1)
    visited = [[-1] * m for _ in range(n)]
    
    queue = deque([(0, 0)]) # 시작점 (x, y)
    visited[0][0] = 1        # 시작 위치의 거리는 1
    
    while queue:
        x, y = queue.popleft()
        
        # 목적지에 도달했다면 현재까지의 거리를 반환
        if x == n - 1 and y == m - 1:
            return visited[x][y]
        
        # 4방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 맵 범위 안에 있고, 벽이 아니며(1), 아직 방문하지 않았다면(-1)
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1 and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
                    
    # 모든 탐색이 끝났는데 목적지에 도달하지 못한 경우
    return -1