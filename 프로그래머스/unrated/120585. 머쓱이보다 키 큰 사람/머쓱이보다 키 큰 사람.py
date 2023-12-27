def solution(array, height):
    answer = 0
    for k in array:
        if height < k:
            answer += 1
    return answer