def solution(a, b):
    x = 2*a*b
    a, b = str(a), str(b)
    y = int(a+b)
    return max(x, y)