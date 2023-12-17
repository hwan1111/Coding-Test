def solution(a, b):
    inner_pro = sum(a[i] * b[i] for i in range(len(a)))
    return inner_pro