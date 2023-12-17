def solution(x, n):
    if x > 0:
        return list(i for i in range(x, x*n + 1, x))
    elif x == 0:
        return [x]*n
    else:
        return list(i for i in range(x, x*n - 1, x))