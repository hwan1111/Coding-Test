from collections import deque

N = int(input())
balloons = deque(enumerate(map(int, input().split())))

result = []

while balloons:
    idx, move = balloons.popleft()
    result.append(str(idx + 1))

    if not balloons:
        break

    if move > 0:
        balloons.rotate(-(move - 1))
    else:
        balloons.rotate(-move)

print(" ".join(result))