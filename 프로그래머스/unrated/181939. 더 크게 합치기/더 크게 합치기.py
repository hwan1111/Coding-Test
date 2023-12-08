def solution(a, b):
    a, b = str(a), str(b)
    x = int(a+b)
    y = int(b+a)
    if x >= y:
        return x
    else:
        return y