def solution(my_strings, s, e):
    front = my_strings[:s]
    back = my_strings[e+1:]
    center = my_strings[s:e+1]
    reverse = center[::-1]
    answer = front + reverse + back
    return answer