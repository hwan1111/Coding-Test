def solution(numLog):
    answer = []
    for idx in range(1, len(numLog)):
        d = numLog[idx] - numLog[idx-1]
        if d == 1:
            answer.append('w')
        elif d == -1:
            answer.append('s')
        elif d == 10:
            answer.append('d')
        elif d == -10:
            answer.append('a')
        
    return ''.join(answer)