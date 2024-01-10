def Fibo(n):
    first, second = 0, 1
    for _ in range(n):
        first, second = second, first + second
    
    return first

def solution(n):
    return Fibo(n)%1234567