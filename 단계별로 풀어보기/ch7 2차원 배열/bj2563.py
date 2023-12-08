#2563, 색종이
#2차원 배열을 활용하여 색종이로 평면을 덮는 문제
#집합문제 같음(합집합)

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