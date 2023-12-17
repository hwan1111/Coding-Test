def solution(n):
    str_n = str(n)[::-1]
    return [int(str_n[i]) for i in range(len(str_n))]