def solution(food):
    pre_result = ''
    for i in range(1, len(food)):
        pre_result += f'{i}' * (food[i]//2)
    
    answer = pre_result + '0' + pre_result[::-1]

    return answer