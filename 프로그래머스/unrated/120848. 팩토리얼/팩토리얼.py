def Fac(i):
    if i == 0 or i == 1:
        return 1
    else:
        return i * Fac(i - 1)

def solution(n):
    i = 0
    while Fac(i) <= n:
        i += 1
    
    return i - 1