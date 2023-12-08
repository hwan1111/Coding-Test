def solution(num_list):
    sum_sq = sum(num_list)**2
    Product = 1
    for idx in range(len(num_list)):
        Product *= num_list[idx]
    
    if sum_sq > Product:
        return 1
    else:
        return 0