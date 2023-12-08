A = []

for i in range(9):
    row_A = list(map(int, input().split()))
    A.append(row_A)

max_value = None
max_row, max_col = None, None

for i in range(9):
    for j in range(9):
        if max_value is None or A[i][j] > max_value:
            max_value = A[i][j]
            max_row, max_col = i, j

print(max_value)
print(max_row+1, max_col+1)