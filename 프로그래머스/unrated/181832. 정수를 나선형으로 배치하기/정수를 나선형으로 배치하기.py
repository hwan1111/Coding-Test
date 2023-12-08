def solution(n):
    # n x n 크기의 이차원 배열 초기화
    result = [[0] * n for _ in range(n)]
    
    # 각 방향별로 이동을 정의 (우, 하, 좌, 상)
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # 초기 위치 및 이동 방향 설정
    row, col = 0, 0
    direction_idx = 0
    
    for num in range(1, n**2 + 1):
        result[row][col] = num
        
        # 다음 위치 계산
        next_row, next_col = row + directions[direction_idx][0], col + directions[direction_idx][1]
        
        # 다음 위치가 범위를 벗어나거나 이미 값이 채워진 경우 방향 전환
        if next_row < 0 or next_row >= n or next_col < 0 or next_col >= n or result[next_row][next_col] != 0:
            direction_idx = (direction_idx + 1) % 4  # 방향을 우, 하, 좌, 상 순서로 변경
            next_row, next_col = row + directions[direction_idx][0], col + directions[direction_idx][1]
        
        row, col = next_row, next_col

    return result