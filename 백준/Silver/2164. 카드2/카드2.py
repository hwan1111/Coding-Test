from collections import deque

N = int(input())

stack = deque([i for i in range(1, N + 1)])

while len(stack) > 1:
    stack.popleft()
    stack.append(stack.popleft())

print(stack[0])