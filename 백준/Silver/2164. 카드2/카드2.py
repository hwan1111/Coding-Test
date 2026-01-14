import sys

N = int(sys.stdin.readline())

if N == 1:
    print(1)
else:
    # N의 비트 길이를 이용해 가장 큰 2의 거듭제곱을 바로 계산
    # 예: N=6(110(2)) -> bit_length=3 -> 1 << (3-1) = 100(2) = 4
    highest_power_of_2 = 1 << (N.bit_length() - 1)
    
    L = N - highest_power_of_2
    
    if L == 0:
        print(N)
    else:
        print(2 * L)