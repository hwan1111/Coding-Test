def solution(q, r, code):
    answer = ''
    for idx, value in enumerate(code):
        if idx%q == r:
            answer += value
    
    return answer