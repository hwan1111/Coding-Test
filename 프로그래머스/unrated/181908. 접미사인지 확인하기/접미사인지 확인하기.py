def solution(my_strings, is_suffix):
    answer = 0
    suffix = []
    for i in range(len(my_strings)):
        suffix.append(my_strings[i:])
    if is_suffix in suffix:
        answer = 1

    return answer