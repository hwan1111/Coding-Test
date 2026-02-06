def solution(n, computers):
    def dfs(node):
        visited[node] = True
        for connect in range(n):
            if computers[node][connect] == 1 and visited[connect] is False:
                dfs(connect)
    
    visited = [False] * n
    answer = 0
    for i in range(n):
        if visited[i] is False:
            dfs(i)
            answer += 1
            
    return answer