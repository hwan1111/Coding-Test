import sys
from collections import deque

# 입출력 속도 향상
input = sys.stdin.readline

def fast_print(x):
    sys.stdout.write(str(x) + '\n')

queue = deque([])

# 명령어 매핑 (lambda를 사용하여 실행 가능한 함수 형태로 저장)
user_input_manual = {
    'pop': lambda: queue.popleft() if queue else -1,
    'size': lambda: len(queue),
    'empty': lambda: 1 if not queue else 0,
    'front': lambda: queue[0] if queue else -1,
    'back': lambda: queue[-1] if queue else -1
}

N_str = input().strip()
if N_str:
    N = int(N_str)
    for _ in range(N):
        line = input().split()
        if not line:
            continue
            
        cmd = line[0]

        if cmd == 'push':
            queue.append(line[1])
        else:
            # 딕셔너리에서 함수를 꺼내 즉시 실행하고 출력
            result = user_input_manual[cmd]()
            fast_print(result)