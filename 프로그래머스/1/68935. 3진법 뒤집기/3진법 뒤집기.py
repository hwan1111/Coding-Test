def solution(n):
    reversed_Trit = []
    while n > 0:
        reversed_Trit.append(n%3)
        n //= 3
    
    answer = 0

    for i in range(len(reversed_Trit)):
        answer += (3**(len(reversed_Trit) - i - 1)) * reversed_Trit[i]
    
    return answer