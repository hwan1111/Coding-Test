import math

def solution(n, a, b):
    answer = 1

    while True:
        # A와 B가 이길 때까지 반복
        if abs(a - b) == 1 and (a // 2 != b // 2):
            return answer
        else:
            # 다음 라운드에 대한 번호 갱신
            answer += 1
            a = (a + 1) // 2
            b = (b + 1) // 2
