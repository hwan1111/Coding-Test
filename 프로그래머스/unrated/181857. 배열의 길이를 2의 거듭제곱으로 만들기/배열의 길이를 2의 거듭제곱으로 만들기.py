import math
def solution(arr):
    if (math.log2(len(arr))%1) == 0:
        return arr
    else:
        for i in range(len(arr), next_exp(len(arr))):
            arr.append(0)
        return arr 

def next_exp(n):
    if n and not (n & (n-1)):   #n이 이미 2의 거듭제곱수일 경우
        return n
    
    #입력된 숫자보다 큰 최소의 2의 거듭제곱수 찾음
    result = 1
    while result < n:
        result <<= 1
    
    return result