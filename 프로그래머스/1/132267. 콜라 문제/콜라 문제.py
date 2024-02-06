def solution(a, b, n):
    answer = 0
    while n >= a:
        remain = n % a
        n = b * (n//a)
        answer += n
        n += remain
    
    return answer