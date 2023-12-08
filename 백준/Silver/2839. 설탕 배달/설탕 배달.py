def sugar(N):
    result = []

    for i in range(N//3 +1):
        remaining = N - i * 3
        if remaining % 5 == 0:
            j = remaining // 5
            result.append((i, j))
    
    if len(result) == 0:
        return -1
    else:
        min_sum = min(sum(pair) for pair in result)
        return min_sum

N = int(input())
print(sugar(N))