import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    ps = input().strip()
    stack = []
    balanced = True

    for char in ps:
        if char == '(':
            stack.append(char)
        else:  # char == ')'
            if stack:
                stack.pop()
            else:
                balanced = False
                break

    if balanced and not stack:
        print("YES")
    else:
        print("NO")