def solution(s):
    s = s.lower()
    s_list = list(s)
    cnt_p = s_list.count('p')
    cnt_y = s_list.count('y')

    return True if cnt_p == cnt_y else False