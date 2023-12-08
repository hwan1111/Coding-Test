import math
def zoac(H, W, N, M):
    row = math.ceil(H/(N+1))
    col = math.ceil(W/(M+1))
    answer = row * col
    return answer
    
H, W, N, M = map(int, input().split())
print(zoac(H, W, N, M))