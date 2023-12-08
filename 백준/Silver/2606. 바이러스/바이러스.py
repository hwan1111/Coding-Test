import sys
input = sys.stdin.readline

def DFS(graph, node, visited=None):
    if visited is None:
        visited = []

    visited.append(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            DFS(graph, neighbor, visited)

    return len(visited)-1

n = int(input())    #컴퓨터 개수
computer = [[] for i in range(n+1)]   #1번부터 n번까지 번호부여된 컴퓨터들
networks = int(input())

for i in range(networks):
    v1, v2 = map(int, map(lambda x: x.rstrip(), input().split()))
    computer[v1].append(v2)
    computer[v2].append(v1)

print(DFS(computer, 1))