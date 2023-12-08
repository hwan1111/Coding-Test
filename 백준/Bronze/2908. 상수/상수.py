X, Y = map(str, input().split())
reversed_X = X[::-1]; reversed_Y = Y[::-1]
X1 = int(reversed_X); Y1 = int(reversed_Y)
if X1 > Y1 : print(X1)
else : print(Y1)