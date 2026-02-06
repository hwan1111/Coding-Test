def solution(n, computers):
    parent = [i for i in range(n)]

    def find(x):
        if parent[x] == x:
            return x
        # 경로 압축: 대장을 찾으면서 부모 정보를 대장으로 갱신
        parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            parent[rootX] = rootY  # 두 팀을 합침
            return True # 합치기 성공
        return False # 이미 같은 팀

    # 모든 연결 관계를 확인하며 합치기
    for i in range(n):
        for j in range(i + 1, n):
            if computers[i][j] == 1:
                union(i, j)

    # 마지막에 '대장이 자기 자신인 사람'의 수를 세면 네트워크 개수!
    return len([i for i in range(n) if parent[i] == i])