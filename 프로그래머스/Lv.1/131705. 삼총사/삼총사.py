from itertools import combinations

def solution(number):
    answer = 0
    trios = [i for i in combinations(number, 3)]
    for trio in trios:
        if sum(trio) == 0:
            answer += 1
    
    return answer