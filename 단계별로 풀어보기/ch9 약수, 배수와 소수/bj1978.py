#1978, 소수 찾기
#2부터 X-1까지 모두 나눠서 X가 소수인지 판별하는 문제 1

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

cnt = 0
n = int(input())
num = list(map(int, input().split()))
for i in range(n):
    if is_prime(num[i]):
        cnt += 1
print(cnt)