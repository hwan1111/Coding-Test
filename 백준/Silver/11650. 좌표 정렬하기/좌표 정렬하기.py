N = int(input())
points = []

for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

sorted_points = sorted(points, key=lambda point: (point[0], point[1]))

for x, y in sorted_points:
    print(x, y)