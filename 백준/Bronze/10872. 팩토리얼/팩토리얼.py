def Fac(N) :
    if N == 0 :
        return 1
    return N * Fac(N-1)

N = int(input())
print(f"{Fac(N)}")