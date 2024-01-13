def gcd(n, m):
    while m:
        n, m = m, n%m
    
    return n

def solution(a, b):
    common_factor = gcd(a, b)
    a //= common_factor
    b //= common_factor

    while b%2 == 0:
        b //= 2
    while b%5 == 0:
        b //= 5
    
    if b == 1:
        return 1
    else:
        return 2