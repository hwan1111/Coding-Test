# 18258
# 큐 2
from collections import deque
import sys

input = sys.stdin.readline

def fast_print(x):
    sys.stdout.write(str(x)+'\n')

queue = deque([])

user_input_manual = {
    'pop': lambda: queue.popleft() if queue else -1,
    'size': lambda: len(queue),
    'empty': lambda: 1 if not queue else 0,
    'front': lambda: queue[0] if queue else -1,
    'back': lambda: queue[-1] if queue else -1
}

N = int(input().strip())
for _ in range(N):
    user_input = input().split()
    cmd = user_input[0]

    if cmd == 'push':
        queue.append(user_input[1])
    else:
        fast_print(user_input_manual[cmd]())