def solution(num_list):
    answer = 0
    temp = [1]*len(num_list)
    while temp != num_list:
        temp = num_list.copy()
        for i in range(len(num_list)):
            if num_list[i]%2 == 0:
                num_list[i] //= 2
                answer += 1
            else:
                if num_list[i] == 1:
                    pass
                else:
                    num_list[i] = (num_list[i]-1)/2
                    answer += 1

    return answer
