def solution(s):
    answer = []

    for el in s.split():
        if el == 'Z':
            answer.pop()
            continue
        answer.append(int(el))

    return sum(answer)