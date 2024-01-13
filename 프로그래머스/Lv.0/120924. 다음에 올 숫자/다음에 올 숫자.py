def solution(common):
    if (common[2]+common[0])/2 == common[1]:
        d = common[1] - common[0]
        return d + common[-1]
    else:
        r = common[2]/common[1]
        return r * common[-1]