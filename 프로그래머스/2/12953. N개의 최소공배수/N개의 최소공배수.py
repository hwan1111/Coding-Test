def GCD(a, b):
    while b:
        a, b = b, a%b
    
    return a

def LCM(a, b):
    return (a * b) // GCD(a, b)

def solution(arr):
    answer = LCM(arr[0], arr[1])
    for i in range(2, len(arr)):
        answer = LCM(answer, arr[i])
    
    return answer