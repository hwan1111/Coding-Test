def divisors_of_N(n):
    divisors = []
    for i in range(1, n+1):
        if n%i == 0:
            divisors.append(i)
    
    return divisors

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if len(divisors_of_N(i))%2 == 0:
            answer += i
        else:
            answer -= i
    
    return answer