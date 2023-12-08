#2480, 주사위 세개
#조건에 따라 상금을 계산하는 문제

def Dice(a: int, b: int, c : int):
    if a == b :
        if b == c :
            return 10000 + a*1000
        else : return 1000 + a*100
    else :
        if b == c : return 1000 + b*100
        else : return max(a,b,c)*100

a, b, c = map(int, input().split())
Dice(a, b, c)