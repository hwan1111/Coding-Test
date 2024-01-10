def solution(board):
    n = len(board)
    answer = 0
    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < n
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                cnt_mine = 0

                dir = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
                for dx, dy in dir:
                    nx, ny = i + dx, j + dy
                    if is_valid(nx, ny) and board[nx][ny] == 1:
                        cnt_mine += 1
                
                if cnt_mine == 0:
                    answer += 1
    
    return answer