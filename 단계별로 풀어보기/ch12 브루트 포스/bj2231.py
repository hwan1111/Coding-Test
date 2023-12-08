#2231, 분해합
#모든 경우를 시도하여 N의 생성자를 구하는 문제

N = int(input())

for i in range(1, N+1):
    num = sum(map(int, str(i)))
    total = i + num

    if total == N:
        print(i)
        break
    if i == N:
        print(0)