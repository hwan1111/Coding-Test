def solution(arr):
    answer = 0
    string = ''.join(str(arr))
    for s in string:
        if s == '7':
            answer += 1
    
    return answer