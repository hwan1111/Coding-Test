def solution(n):
    #answer = n과 6의 최소공배수 // 6
    return lcm(n, 6)//6

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a*b) // gcd(a, b)