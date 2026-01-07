import sys

# 1. [전역 설정] 문제에서 주어진 최대 범위까지 소수를 미리 구해놓습니다.
# n의 최대 범위가 1,000,000이라고 가정합니다.
MAX = 1000000
is_prime = [True] * (MAX + 1)
is_prime[0] = is_prime[1] = False

# 에라토스테네스의 체: 이 루프는 프로그램 실행 시 단 한 번만 돕니다.
for i in range(2, int(MAX**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, MAX + 1, i):
            is_prime[j] = False

def solve():
    # 2. 입력을 받습니다.
    line = sys.stdin.readline()
    if not line:
        return
    n = int(line)
    
    answer = 0
    # 3. p는 2부터 시작해도 되지만, 문제 조건(2보다 큰 짝수, 홀수 소수 파티션)에 따라
    # 보통 2를 제외한 3부터 n/2까지 확인합니다.
    # (참고: n=4일 때 2+2를 포함해야 한다면 범위를 2부터 시작하면 됩니다.)
    for p in range(2, n // 2 + 1):
        if is_prime[p]:  # p가 소수이고
            q = n - p    # 짝수 n에서 p를 뺀 남은 수 q가
            if is_prime[q]:  # 소수라면 파티션 성립!
                answer += 1
            
    sys.stdout.write(f'{answer}\n')

T = int(sys.stdin.readline())
for _ in range(T):
    solve()