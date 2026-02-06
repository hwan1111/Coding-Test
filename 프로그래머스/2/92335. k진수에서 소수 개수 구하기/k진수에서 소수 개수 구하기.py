def k_decimal(n, k):
    answer = ''
    while n > 0:
        answer += str(n%k)
        n //= k
    
    return answer[::-1]

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    prime_set = k_decimal(n, k).split('0')
    answer = 0
    
    for num in prime_set:
        if num == '':
            pass
        else:
            if is_prime(int(num)) is True:
                answer += 1
    
    return answer