#2566, 최댓값
#최댓값을 2차원에서 찾는 문제

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

#넘파이를 이용해 위의 코드의 문제(탐색시간 多)를 해결

import numpy as np

A = []

for i in range(9):
    row_A = list(map(int, input().split()))
    A.append(row_A)

# 2차원 리스트를 NumPy 배열로 변환
A = np.array(A)

# 최대값과 그 위치를 찾음
max_value = np.max(A)
max_indices = np.argwhere(A == max_value)[0]  # 첫 번째 발견된 위치를 선택

# 위치에 1을 추가
max_indices = [x + 1 for x in max_indices]

print(max_value)
for i in range(2):
    print(f"{max_indices[i]}", end = " ")