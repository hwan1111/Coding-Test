import sys
from collections import deque

input = sys.stdin.readline

def fast_print(x):
    sys.stdout.write(str(x) + '\n')

queue = deque([])

user_input_manual = {
    '3': lambda: queue.popleft() if queue else -1,
    '4': lambda: queue.pop() if queue else -1,
    '5': lambda: len(queue),
    '6': lambda: 1 if not queue else 0,
    '7': lambda: queue[0] if queue else -1,
    '8': lambda: queue[-1] if queue else -1
}

N_str = input().strip()
if N_str:
    for _ in range(int(N_str)):
        line = input().split()

        if  not line:
            continue

        cmd = line[0]

        if cmd == '1':
            queue.appendleft(line[1])
        elif cmd == '2':
            queue.append(line[1])
        else:
            result = user_input_manual[cmd]()
            fast_print(result)