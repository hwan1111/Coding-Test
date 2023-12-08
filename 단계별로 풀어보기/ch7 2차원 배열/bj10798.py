#10798, 세로읽기
#문자열의 배열을 다루는 문제

A = []
for _ in range(5):
    row_A = input()
    A.append(row_A)

for col in range(15):
    for row in range(5):
        if col < len(A[row]): print(A[row][col], end = "")      #등호를 넣어야하나?
        else: pass