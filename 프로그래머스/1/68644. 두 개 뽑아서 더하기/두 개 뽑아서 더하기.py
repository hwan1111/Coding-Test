from itertools import combinations

def solution(nums):
    answer = []
    combination_list = list(combinations(nums, 2))
    for i, j in combination_list:
        answer.append(i+j)

    return sorted(set(answer))