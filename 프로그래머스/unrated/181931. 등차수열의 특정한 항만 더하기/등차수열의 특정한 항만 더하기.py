def solution(a, d, included):
    answer = 0
    for idx in range(len(included)):
        answer += int(included[idx])*(d*(idx)+a)
    
    return answer