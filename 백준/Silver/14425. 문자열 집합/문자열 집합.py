import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = set()

for i in range(N):
    S_i = input().strip()
    S.add(S_i)

answer = 0
for i in range(M):
    check_i = input().strip()
    if check_i in S:
        answer += 1

print(answer)