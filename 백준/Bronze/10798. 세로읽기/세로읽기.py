A = []
for _ in range(5):
    row_A = input()
    A.append(row_A)

for col in range(15):
    for row in range(5):
        if col < len(A[row]): print(A[row][col], end = "")
        else: pass