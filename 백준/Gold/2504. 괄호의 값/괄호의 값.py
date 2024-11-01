def calculate_bracket_value(bracket_string):
    stack = []
    value = 0  # 최종 값을 저장할 변수
    temp = 1   # 중간 계산값을 저장할 변수

    for i in range(len(bracket_string)):
        token = bracket_string[i]

        if token == '(':
            stack.append(token)
            temp *= 2

        elif token == '[':
            stack.append(token)
            temp *= 3

        elif token == ')':
            if not stack or stack[-1] != '(':
                return 0  # 올바르지 않은 괄호열
            if bracket_string[i - 1] == '(':
                value += temp
            stack.pop()
            temp //= 2

        elif token == ']':
            if not stack or stack[-1] != '[':
                return 0  # 올바르지 않은 괄호열
            if bracket_string[i - 1] == '[':
                value += temp
            stack.pop()
            temp //= 3

    # 스택이 비어있지 않으면 괄호가 완전히 짝지어지지 않음
    if stack:
        return 0

    return value


exp = input()
print(calculate_bracket_value(exp))