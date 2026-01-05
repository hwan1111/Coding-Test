# 2485
# 가로수

import sys

def GCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# 입력을 빠르게 받기 위해 sys.stdin.readline 사용
N = int(sys.stdin.readline())
tree_positions = []
for _ in range(N):
    tree_positions.append(int(sys.stdin.readline()))

# 1. 모든 간격(distances)을 먼저 구함.
distances = []
for i in range(1, N):
    distances.append(tree_positions[i] - tree_positions[i-1])

# 2. 첫 번째 간격을 초기 gcd로 설정하고 나머지 간격들과의 GCD를 구함.
g = distances[0]
for j in range(1, len(distances)):
    g = GCD(g, distances[j])

# 3. 전체 필요한 나무 수 계산
# 전체 간격 수 = (마지막 나무 - 첫 나무) // g
# 필요한 총 나무 수 = (전체 간격 수) + 1
# 새로 심을 나무 = (필요 총 나무 수) - (이미 있는 나무 수)
ans = ((tree_positions[-1] - tree_positions[0]) // g) + 1 - N
print(ans)