# 1764
# 듣보잡
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
non_heard = set()
non_seen = set()

for _ in range(N):
    non_heard.add(input().strip())

for _ in range(M):
    non_seen.add(input().strip())

non_heard_and_seen = non_heard.intersection(non_seen)

print(len(non_heard_and_seen))
for name in sorted(non_heard_and_seen):
    print(name)