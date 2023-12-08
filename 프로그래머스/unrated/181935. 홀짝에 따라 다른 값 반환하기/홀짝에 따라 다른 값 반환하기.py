def solution(n):
    answer = 0
    if n%2 == 1:
        i = 1
        while i <= n:
            answer += i
            i += 2
        return answer
    else:
        i = 0
        while i <= n:
            answer += i**2
            i += 2
        return answer