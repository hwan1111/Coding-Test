import sys

# 입력을 더 효율적으로 받기 위해 sys.stdin 사용
lines = sys.stdin.readlines()

for line in lines:
    # 1. 종료 조건: 입력의 끝이 온점 하나(".")인 경우
    if line.rstrip() == ".":
        break
        
    stack = []
    is_balanced = True
    
    for char in line:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                is_balanced = False
                break
        elif char == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                is_balanced = False
                break
                
    # 2. 결과 출력: 스택이 비어 있고, 중간에 잘못된 짝이 없어야 함
    if is_balanced and not stack:
        print("yes")
    else:
        print("no")