def solution(rank, attendance):
    answer = 0
    tmp = []
    for i, v in enumerate(rank):
        if attendance[i]:
            tmp.append(rank[i])
    
    tmp.sort()
    a, b, c = 0, 0, 0
    for i, v in enumerate(rank):
        if v == tmp[0]:
            a = i
        elif v == tmp[1]:
            b = i
        elif v == tmp[2]:
            c = i

    return 10000 * a + 100 * b + c
