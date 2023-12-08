#2581, 소수
#2부터 X-1까지 모두 나눠서 X가 소수인지 판별하는 문제 2

def sieve_of_eratosthenes(m, n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    primes = [i for i in range(m, n + 1) if is_prime[i]]
    return primes

m = int(input())
n = int(input())

prime = sieve_of_eratosthenes(m, n)
if len(prime) != 0:
    print(sum(prime))
    print(min(prime))
else:
    print(-1)
