import sys

input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
    user_input = input().split()
    order = int(user_input[0]) # 첫 번째 숫자는 항상 명령어

    if order == 1:
        # 2. '1 X' 형태일 때 X를 스택에 넣음
        X = int(user_input[1])
        stack.append(X)
        
    elif order == 2:
        # 3. 스택에서 빼고 출력 (pop 사용)
        if stack:
            print(stack.pop())
        else:
            print(-1)
            
    elif order == 3:
        # 4. 개수 출력
        print(len(stack))
        
    elif order == 4:
        # 5. 비었으면 1, 아니면 0 (로직 수정)
        print(1 if not stack else 0)
        
    elif order == 5:
        # 6. 맨 위 확인만 하고 출력 (제거 X)
        if stack:
            print(stack[-1])
        else:
            print(-1)