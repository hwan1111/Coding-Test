def solution(s):
    j = [int(i) for i in s.split()]
    return f"{min(j)} {max(j)}"