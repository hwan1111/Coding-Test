import sys
input = sys.stdin.readline

N, M = map(int, input().split())
Basket_Num = [i for i in range(1, N + 1)]
for _ in range(M) :
    i, j = map(int, input().split())
    Basket_Num[i - 1 : j] = reversed(Basket_Num[i - 1 : j])
for i in Basket_Num :
    print(i, end = " ")