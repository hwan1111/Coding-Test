def solution(a, b, c, d):
    dice = [a, b, c, d]
    dice.sort()
    arr = list(set(dice))

    if len(arr) == 1:
        return 1111*arr[0]
    elif len(arr) == 2:
        if dice[0] == dice[2]:
            return (10*arr[0] + arr[1])**2
        elif dice[1] == dice[3]:
            return (10*arr[1] + arr[0])**2
        elif dice[0] == dice[1] and dice[2] == dice[3]:
            return (arr[0] + arr[1]) * abs(arr[1] - arr[0])
    elif len(arr) == 3:
        if dice[0] == dice[1]:
            return (arr[1] * arr[2])
        elif dice[1] == dice[2]:
            return (arr[2] * arr[0])
        elif dice[2] == dice[3]:
            return (arr[0] * arr[1])
    elif len(arr) == 4:
        return min(arr)