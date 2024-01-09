def solution(my_str, n):
    answer = []
    for i in range(len(my_str)//n + 1):
        answer.append(my_str[i * n: i * n+n])
    
    if answer[-1] == '':
        answer.pop()
    return answer