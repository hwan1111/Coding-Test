def solution(n, s):
    answer = []
    if n > s:
        answer = [-1]
    else:
        front = [(s-(s%n))/n]*(n-(s%n))
        back = [(s+(n-(s%n)))/n]*(s%n)
        answer = front + back
        
    return answer