#2869, 달팽이는 올라가고 싶다
#달팽이의 움직임을 계산하는 문제🐌

A, B, V = map(int, input().split())

if V < A :
    print(1)
else:
    if (V-A)%(A-B) == 0:
        print((V-A)//(A-B)+1)
    else:
        print((V-A)//(A-B)+2)