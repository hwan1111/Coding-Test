from itertools import combinations

def incline(dot0, dot1):
    return abs(dot0[1] - dot1[1]) / abs(dot0[0] - dot1[0])

def solution(dots):
    for a, b in combinations(combinations(dots, 2), 2):
        if set(tuple(_) for _ in a).isdisjoint(set(tuple(_) for _ in b)):
            if incline(*a) == incline(*b):
                return 1

    return 0