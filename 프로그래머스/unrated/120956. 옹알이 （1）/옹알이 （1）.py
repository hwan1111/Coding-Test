from itertools import permutations

def solution(babbling):
    answer = 0
    speek = ['aya', 'ye', 'woo', 'ma']
    words = []
    
    for i in range(1, len(speek) + 1):
        for j in permutations(speek, i):
            words.append(''.join(j))

    for bab in babbling:
        if bab in words:
            answer += 1
            
    return answer