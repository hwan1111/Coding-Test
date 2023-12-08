#최빈값 구하기

def solution(arr):
    cnt = {}
    for item in arr:
        if item in cnt:
            cnt[item] += 1
        else:
            cnt[item] = 1
    
    max_cnt = max(cnt.values())
    modes = [key for key, value in cnt.items() if value == max_cnt]

    if len(modes) > 1:
        return -1
    else:
        return modes[0]