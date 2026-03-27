import sys
input = sys.stdin.readline

N, M = map(int, input().split())
parent = list(range(N + 1))

def find(k):
    if parent[k] != k:
        parent[k] = find(parent[k])
    return parent[k]

def union(a, b):
    rootA = find(a)
    rootB = find(b)
    if rootA != rootB:
        parent[rootB] = rootA

for _ in range(M):
    u, v = map(int, input().split())
    union(u, v)

# 자기 자신이 루트인 노드의 수 = 연결 요소 개수
print(sum(find(i) == i for i in range(1, N + 1)))
