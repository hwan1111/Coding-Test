def solution(my_strings):
    answer = []
    for i in range(len(my_strings)):
        answer.append(my_strings[i:])
    answer.sort()
    return answer