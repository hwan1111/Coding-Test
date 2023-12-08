#19532, 수학은 비대면강의입니다
#모든 x와 모든 y를 시도하여 해를 구하는 문제

a, b, c, d, e, f = map(int, input().split())
result = []

for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a*x + b*y == c and d*x + e*y == f:
            result = [x, y]
            break

for i in range(len(result)):
    print(result[i], end = " ")