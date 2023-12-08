def solution(n):
    answer = []
    def hanoi(n, start, via, target):
        if n == 1:
            answer.append([start, target])
        else:
            hanoi(n-1, start, target, via)
            hanoi(1, start, via, target)
            hanoi(n-1, via, start, target)
    hanoi(n, 1, 2, 3)
    return answer