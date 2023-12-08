def DFS(x, y):
    result = []
    
    if x <= -1 or x >= N or y <= -1 or y >= N:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        cnt.append(1)
        
        DFS(x+1, y)
        DFS(x-1, y)
        DFS(x, y+1)
        DFS(x, y-1)
        return True
    return False

N = int(input())
graph = []
cnt = []
for _ in range(N):
    graph.append(list(map(int, input())))

result = 0
result_list = []

for i in range(N):
    for j in range(N):
        if DFS(i, j):
            result += 1
            result_list.append(len(cnt))
            cnt = []

print(result)
result_list.sort()
for i in result_list:
    print(i)