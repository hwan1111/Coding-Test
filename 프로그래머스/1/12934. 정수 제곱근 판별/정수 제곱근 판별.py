import math
def solution(n):
    x = math.sqrt(n)
    if x.is_integer():
        return (x+1)**2
    else:
        return -1