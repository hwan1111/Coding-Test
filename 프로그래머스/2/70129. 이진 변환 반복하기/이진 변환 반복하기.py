def solution(s):
    answer = []
    cnt_bin = 0
    cnt_removed_zero = 0

    while s != '1':
        cnt_removed_zero += s.count('0')
        s = s.replace('0', '')
        l = len(s)
        s = bin(l)[2:]
        cnt_bin += 1

    return [cnt_bin, cnt_removed_zero]