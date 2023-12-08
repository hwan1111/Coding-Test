#9063, 대지
#옥구슬을 모두 포함하는 직사각형을 찾는 문제
"""
import sys
input = sys.stdin.readline
"""
n = int(input())
X = []
Y = []
for i in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

area = (max(X)-min(X))*(max(Y)-min(Y))
print(area)