N = int(input())

dp = [0] * (N + 1)

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + 1          # 연산 3: 1 빼기
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)   # 연산 2: 2로 나누기
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)   # 연산 1: 3으로 나누기

print(dp[N])