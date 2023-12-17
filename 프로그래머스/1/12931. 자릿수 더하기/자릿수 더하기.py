def solution(n):
    n = str(n)
    return sum(int(n[i]) for i in range(len(n)))