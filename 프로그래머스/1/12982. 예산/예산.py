def solution(d, budget):
    d.sort()
    sum = 0

    for i in range(len(d)):
        sum += d[i]
        if budget < sum:
            return i

    return len(d)