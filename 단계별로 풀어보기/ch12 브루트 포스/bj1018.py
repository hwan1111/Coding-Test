#1018, 체스판 다시 칠하기
#체스판을 만드는 모든 경우를 시도하여 최적의 방법을 찾는 문제

n, m = map(int, input().split())
board = []
for _ in range(n):
    row_of_board = list(input())
    board.append(row_of_board)

min_changes = float('inf')

for i in range(n-7):
    for j in range(m-7):
        cnt_w = 0
        for row in range(i, i+8):
            for col in range(j, j+8):
                if (row + col) % 2 == 0 and board[row][col] == 'B':
                    cnt_w += 1
                elif (row + col) % 2 == 1 and board[row][col] == 'W':
                    cnt_w += 1

        cnt_b = 0
        for row in range(i, i+8):
            for col in range(j, j+8):
                if (row + col) % 2 == 0 and board[row][col] == 'W':
                    cnt_b += 1
                elif (row + col) % 2 == 1 and board[row][col] == 'B':
                    cnt_b += 1
        min_changes = min(min_changes, cnt_w, cnt_b)

print(min_changes)