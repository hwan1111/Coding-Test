def solution(n):
    answer = []

    while n%2 == 0:
        answer.append(2)
        n //= 2
    
    for i in range(3, int(n**0.5) + 1, 2):
        while n%i == 0:
            answer.append(i)
            n //= i
    
    if n > 2:
        answer.append(n)

    answer = sorted(list(set(answer)))
    return answer