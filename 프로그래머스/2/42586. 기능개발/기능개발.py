import math

def solution(progresses, speeds):
    result = []
    days = [math.ceil((100 - progresses[i]) / speeds[i])  for i in range(len(speeds))]
    
    max = days[0]
    cnt = 0
    for day in days:
        if day <= max:
            cnt += 1
        else:
            if cnt > 0:
                result.append(cnt)
            max = day
            cnt = 1
    
    if cnt > 0:
        result.append(cnt)
    
    return result