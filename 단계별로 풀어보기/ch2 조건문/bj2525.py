#2525, 오븐 시계
#범위가 더 넓은 시간 계산 문제

def OvenTimer(A, B, C):
    A += C//60
    B += C%60

    if B >= 60:
        A += 1
        B -= 60
    if A >= 24:
        A -= 24

    return print(A, B)

A, B = map(int, input().split())
C = int(input())
OvenTimer(A, B, C)
