def solution(k, tangerine):
    answer = 0
    unique_size = {}
    for i in tangerine:
        if i in unique_size:
            unique_size[i] += 1
        else:
            unique_size[i] = 1
    
    unique_size = dict(sorted(unique_size.items(), key=lambda x: x[1], reverse=True))
    for i in unique_size:
        if k <= 0:
            return answer
        k -= unique_size[i]
        answer += 1
    
    return answer