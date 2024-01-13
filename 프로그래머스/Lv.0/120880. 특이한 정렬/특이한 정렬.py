def solution(numlist, n):
    closed_nlist = sorted(numlist, key=lambda x: (abs(n - x), -x))
    return [i for i in closed_nlist]