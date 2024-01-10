def solution(sides):
    possible_side = [i for i in range(max(sides), sum(sides))] + [i for i in range(max(sides) - min(sides) + 1, max(sides))]
    return len(set(possible_side))