from collections import Counter

def solution(k, tangerine):
    answer = 0
    size_cnt = Counter(tangerine)
    result = sorted(list(size_cnt.values()), key=lambda x: abs(x - k))
    
    for i in range(len(result)):
        answer += result[i]
        if answer >= k:
            return i + 1