def solution(n):
    answer = 0
    for i in range(1, n+1, 2):  # n의 홀수 약수 개수 구하기
        if n % i == 0:
            answer += 1
    return answer
