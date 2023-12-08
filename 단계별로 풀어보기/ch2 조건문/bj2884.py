#2884, 알람시계
#시간 계산 문제

def Alram(h, m) :
    if m < 45 :
        if h == 0 :
            h = 23
            m += 15
        else :
            h -= 1
            m += 15
    else :
        m -= 45
    return print(h, m)
h, m = map(int, input().split())

Alram(h, m)