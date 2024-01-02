def solution(my_str):
    answer = []
    for s in my_str:
        if s not in answer:
            answer.append(s)

    return ''.join(answer)