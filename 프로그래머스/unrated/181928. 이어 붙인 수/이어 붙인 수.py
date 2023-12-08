def solution(num_list):
    odd, even = [], []
    for idx in range(len(num_list)):
        if num_list[idx]%2 == 1:
            odd.append(str(num_list[idx]))
        else:
            even.append(str(num_list[idx]))
    
    sum = int(''.join(odd)) + int(''.join(even))
    return sum