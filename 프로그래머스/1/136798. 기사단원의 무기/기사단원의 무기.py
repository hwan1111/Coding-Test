def count_divisors(number):
    cnt = 1
    i = 2
    while i * i <= number:
        exp = 0
        while number % i == 0:
            exp += 1
            number //= i
        
        if exp > 0:
            cnt *= (exp + 1)

        i += 1
        
    if number > 1:
        cnt *= 2
    
    return cnt

def solution(number, limit,	power):
    answer = 0
    for i in range(1, number+1):
        d = count_divisors(i)
        answer += d if d <= limit else power
    
    return answer