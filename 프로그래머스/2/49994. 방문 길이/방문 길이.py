def solution(dirs: str) -> int:
    visited_paths = set()
    
    # 현재 좌표 (원점)
    x, y = 0, 0
    move = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
    
    for d in dirs:
        dx, dy = move[d]
        nx, ny = x + dx, y + dy
        
        # 좌표 평면 범위 체크 (-5 ~ 5 사이)
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            # 길은 양방향이므로 (현재->다음)과 (다음->현재)를 동일하게 취급해야 함
            # 정렬된 튜플을 사용하여 경로를 저장
            path = tuple(sorted([(x, y), (nx, ny)]))
            visited_paths.add(path)
            
            # 현재 위치 갱신
            x, y = nx, ny
            
    return len(visited_paths)