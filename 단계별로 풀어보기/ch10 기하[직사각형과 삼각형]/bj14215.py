#14215, 세 막대
#가능한 한 둘레가 긴 삼각형을 만드는 문제

a, b, c = list(map(int, input().split()))

max_value = max(a, b, c)
total = a + b + c

if max_value >= (a + b + c) - max_value:
    total = (a + b + c) - max_value
    max_value = (a + b + c) - max_value - 1
    total = total + max_value

print(total)
