def solution(phone_num):
    num = list(phone_num)
    for i in range(len(num)-4):
        num[i] = '*'
    
    return ''.join(num)