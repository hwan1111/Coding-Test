from collections import deque

def solution(A, B):
    A.sort()
    B.sort()
    B = deque(B)

    sum = 0

    for i in range(len(A)):
        sum += A.pop() * B.popleft()
    
    return sum