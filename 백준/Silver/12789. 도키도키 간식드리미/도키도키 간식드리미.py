import sys
from collections import deque

input = sys.stdin.readline

def solve(n):
    students = deque(map(int, input().split()))
    stack = []
    target = 1

    while students:
        if students[0] == target:
            students.popleft()
            target += 1
        elif stack and stack[-1] == target:
            stack.pop()
            target += 1
        else:
            stack.append(students.popleft())
    
    while stack:
        if stack[-1] == target:
            stack.pop()
            target += 1
        else:
            break

    return 'Nice' if not stack else 'Sad'

if __name__ == "__main__":
    n = int(input())
    result = solve(n)
    print(result)