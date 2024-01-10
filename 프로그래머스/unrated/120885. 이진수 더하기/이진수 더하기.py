def solution(bin1, bin2):
    dec1 = sum(int(bin1[i]) * 2 ** (len(bin1) - 1 - i) for i in range(len(bin1)))
    dec2 = sum(int(bin2[i]) * 2 ** (len(bin2) - 1 - i) for i in range(len(bin2)))

    return bin(dec1 + dec2)[2:]