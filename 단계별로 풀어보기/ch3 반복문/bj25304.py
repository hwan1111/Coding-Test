#25304, 영수증
#💸

X = int(input())
N = int(input())
price = 0
for i in range(N) :
    a, b = map(int, input().split())
    c = a*b
    price += c

if X == price : print("Yes")
else : print("No")