def solution(n, m, section):
    answer = 0
    paint_upto = 0  # 지금까지 롤러로 덮어놓은 끝 위치
    
    for s in section:
        if s > paint_upto:        # 새로 칠해야 하는 시작점 발견
            answer += 1
            paint_upto = s + m - 1  # 이번에 덮은 끝 위치

    return answer
