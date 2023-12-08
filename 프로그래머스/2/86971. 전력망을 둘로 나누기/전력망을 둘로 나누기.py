def solution(n, wires):
    graph = [[] for _ in range(n+1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    def dfs(node, visited):
        cnt = 1
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                cnt += dfs(neighbor, visited)
        return cnt

    min_difference = float('inf')

    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)
    
        visited = [False]*(n+1)
        cnt_a = dfs(a, visited)
        cnt_b = dfs(b, visited)

        difference = abs(cnt_a - cnt_b)
        min_difference = min(min_difference, difference)

        graph[a].append(b)
        graph[b].append(a)
    
    return min_difference