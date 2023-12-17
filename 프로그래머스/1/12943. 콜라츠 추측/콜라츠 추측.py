def solution(num):
    cnt = 0
    answer = False
    while num != 1:
        if num%2 == 0:
            num //= 2
        else:
            num = 3*num + 1
        
        cnt += 1

        if cnt > 500:
            break
        
    if num == 1:
        answer = True   
    
    return cnt if answer else -1