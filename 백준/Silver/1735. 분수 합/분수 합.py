# 1735
# 분수 합

import math 

def sum_of_divisor(a, b, c, d):
    numerator = a * d + b * c
    denominator = b * d
    
    gcd = math.gcd(numerator, denominator)

    return numerator // gcd, denominator // gcd

a, b = map(int, input().split())
c, d = map(int, input().split())

numerator, denominator = sum_of_divisor(a, b, c, d)
print(numerator, denominator)