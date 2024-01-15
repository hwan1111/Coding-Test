import sys
input = sys.stdin.readline

n = int(input())
log = {}

for _ in range(n):
    name, action = map(str, input().split())
    if action == 'enter':
        log[name] = True
    else:
        log.pop(name, None)

# 나가지 않은 사람들의 이름을 사전 역순으로 출력
for slave in sorted(log.keys(), reverse=True):
    print(slave)