# 1934
# 최소공배수
import math

def least_common_multiple(A, B):
    gcd = math.gcd(A, B)
    lcm = (A * B) // gcd
    return lcm

T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(least_common_multiple(A, B))