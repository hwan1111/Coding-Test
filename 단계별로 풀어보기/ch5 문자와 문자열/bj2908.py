#2908,상수
#숫자를 뒤집어서 비교하는 문제

a, b = map(str, input().split())

reversed_a = int(a[::-1])
reversed_b = int(b[::-1])

print(max(reversed_a, reversed_b))