def solution(brown, yellow):
    total = brown + yellow  # 전체 카펫의 격자 수
    
    for i in range(1, int(total**0.5) + 1):
        if total % i == 0:
            # i가 전체 격자의 가로 길이, total//i가 세로 길이
            if (i-2) * (total//i-2) == yellow:
                return [max(i, total//i), min(i, total//i)]