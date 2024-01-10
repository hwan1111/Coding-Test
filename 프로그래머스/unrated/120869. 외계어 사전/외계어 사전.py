from itertools import permutations

def solution(spell, dic):
    words = []
    for j in permutations(spell, len(spell)):
        words.append(''.join(j))
    
    answer = 2
    for s in dic:
        if s in words:
            answer = 1
    
    return answer