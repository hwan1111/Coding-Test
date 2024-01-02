def solution(order):
    answer = 0
    order = list(str(order))
    for n in order:
        if n == '3' or n == '6' or n == '9':
            answer += 1
    
    return answer