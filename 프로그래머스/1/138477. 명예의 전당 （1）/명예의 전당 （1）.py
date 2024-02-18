def solution(k, score):
    honer = []
    answer = []

    for i, s in enumerate(score):
        if i < k:
            honer.append(s)
        else:
            if min(honer) < s:
                honer.remove(min(honer))
                honer.append(s)
        answer.append(min(honer))
    
    return answer