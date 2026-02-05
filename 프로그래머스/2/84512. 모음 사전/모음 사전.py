from itertools import product

def solution(word):
    w = ['A', 'E', 'I', 'O', 'U']
    dic = []
    for length in range(1, 6):
        for combination in product(w, repeat=length):
            dic.append(''.join(combination))
            
    return sorted(dic).index(word) + 1