def solution(my_str):
    my_list = my_str.split()
    answer = int(my_list[0])

    for i in range(1, len(my_list)):
        if my_list[i] == '+':
            answer += int(my_list[i+1])
        if my_list[i] == '-':
            answer -= int(my_list[i+1])
    
    return answer