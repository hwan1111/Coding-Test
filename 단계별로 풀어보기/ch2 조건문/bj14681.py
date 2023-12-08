#14681, 사분면 고르기
#점이 어느 사분면에 있는지 알아내는 문제

def Quadrant(x, y) :
    if x > 0 and y > 0 : return print(1)   #1사분면
    if x < 0 and y > 0 : return print(2)   #2사분면
    if x < 0 and y < 0 : return print(3)   #3사분면
    if x > 0 and y < 0 : return print(4)   #4사분면

x, y = map(int, input().split())

Quadrant(x, y)