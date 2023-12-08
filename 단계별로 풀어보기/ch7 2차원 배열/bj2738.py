#2738, 행렬 덧셈
#행렬을 2차원 배열로 만들어 더하는 문제

"""
n, m = map(int, input().split())
A = [[],
     []]
B = [[],
     []]
for i in range(n):
    for j in range(m):
        A[[i][j::]] = map(int, input().split())


C=[[_ for _ in range(2)] for _ in range(3)]
print(C)
"""

n, m = map(int, input().split())

#행렬A 초기화
A = []
for i in range(n):
    row_A = list(map(int, input().split()))
    A.append(row_A)     #2차원으로 확장

#행렬B 초기화
B = []
for i in range(n):
    row_B = list(map(int, input().split()))
    B.append(row_B)     #2차원으로 확장

#결과행렬 초기화
result = []

for i in range(n):
    result_row = []     #행 행렬 초기화
    for j in range(m):
        result_row.append(A[i][j]+B[i][j])
    result.append(result_row)   #2차원으로 확장

for i in range(n):
    for j in range(m):
        print(result[i][j], end = " ")
    print()