def solution(my_str, idx_list):
    answer = ''
    for idx in idx_list:
        answer += my_str[idx]
    
    return answer