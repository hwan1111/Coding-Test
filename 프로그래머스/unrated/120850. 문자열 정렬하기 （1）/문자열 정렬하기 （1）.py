def solution(my_str):
    answer = []
    for i in my_str:
        if i.isdigit():
            answer.append(int(i))

    return sorted(answer)