def solution(A, B):
    for i in range(len(A)):
        shifted_a = A[-i:] + A[:-i]
        if shifted_a == B:
            return i
    
    return -1