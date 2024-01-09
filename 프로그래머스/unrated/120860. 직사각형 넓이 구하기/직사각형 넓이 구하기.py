def solution(dots):
    max_x = max(dots[i][0] for i in range(4))
    max_y = max(dots[i][1] for i in range(4))
    min_x = min(dots[i][0] for i in range(4))
    min_y = min(dots[i][1] for i in range(4))

    return abs(max_x - min_x) * abs(max_y - min_y)