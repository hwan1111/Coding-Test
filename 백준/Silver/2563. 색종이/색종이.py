arr = [[0 for _ in range(100)] for _ in range(100)]
N = int(input())

for _ in range(N):
    x, y = map(int, input().split())

    for row in range(x, x+10):
        for col in range(y, y+10):
            arr[row][col] = 1

area = 0

for i in arr:
    area += i.count(1)

print(area)