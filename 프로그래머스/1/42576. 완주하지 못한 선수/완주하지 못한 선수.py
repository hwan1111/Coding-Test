def solution(participant, completion):
    parti = {}
    for name in participant:
        if name in parti:
            parti[name] += 1
        else:
            parti[name] = 1
        
    for name in completion:
        if name in parti:
            parti[name] -= 1
    
    answer = [i for i in parti.keys() if parti[i] > 0]
    
    return ''.join(answer)