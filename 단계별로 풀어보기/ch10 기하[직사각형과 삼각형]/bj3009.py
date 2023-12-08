#3009, 네 번째 점
#직사각형을 완성하는 문제

X = []
Y = []

for i in range(3):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

for i in range(3):
    if X.count(X[i]) == 1:
        x = X[i]
    if Y.count(Y[i]) == 1:
        y = Y[i]

print(x, y)