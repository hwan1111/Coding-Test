# 1929
# 소수 구하기

def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def solve():
    m, n = map(int, input().split())
    for i in range(m, n+1):
        if is_prime(i) is True:
            print(i)

solve()