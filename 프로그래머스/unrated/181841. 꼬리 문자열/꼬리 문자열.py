def solution(str_list, ex):
    answer = ''
    for String in str_list:
        if ex not in String:
            answer += String
    return answer