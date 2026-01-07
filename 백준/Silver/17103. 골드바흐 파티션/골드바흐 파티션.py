import sys

MAX = 1000000
is_prime = [True] * (MAX + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(MAX**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, MAX + 1, i):
            is_prime[j] = False

def solve():
    line = sys.stdin.readline()
    if not line:
        return
    n = int(line)
    
    answer = 0
    
    for p in range(2, n // 2 + 1):
        if is_prime[p]:  # p가 소수이고
            q = n - p    # 짝수 n에서 p를 뺀 남은 수 q가
            if is_prime[q]:  # 소수라면 파티션 성립!
                answer += 1
            
    sys.stdout.write(f'{answer}\n')

T = int(sys.stdin.readline())
for _ in range(T):
    solve()
