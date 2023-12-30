def solution(balls, share):
    return Fac(balls)/(Fac(balls - share) * Fac(share))
    
def Fac(N):
    if N == 0 or N == 1:
        return 1
    return N*Fac(N-1)