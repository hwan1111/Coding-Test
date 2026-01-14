eigen_num = list(map(int, input().split()))

square = 0
for num in eigen_num:
    square += int(num) ** 2

print(square % 10)