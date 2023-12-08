def solution(my_str, queries):
    my_list = list(my_str)
    for s, e in queries:
        for i in range((e - s + 1) // 2):
            my_list[s + i], my_list[e - i] = my_list[e - i], my_list[s + i]
    my_str = ''.join(my_list)
    return my_str
