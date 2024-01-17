def solution(s):
    last_index = {}
    answer = []

    for idx, char in enumerate(s):
        if char not in last_index or last_index[char] == -1:
            answer.append(-1)
        else:
            answer.append(idx - last_index[char])

        last_index[char] = idx
    
    return answer