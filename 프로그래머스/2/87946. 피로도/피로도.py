from itertools import permutations

def solution(k, dungeons):
    answer = 0
    dungeons = list(permutations(dungeons))
    for posible_order in dungeons:
        count = 0
        curr_k = k
        for min_fatigue, exhaustion_fatigue in posible_order:
            if curr_k >= min_fatigue:
                curr_k -= exhaustion_fatigue
                count += 1
            else:
                break
        
        answer = max(answer, count)

    return answer