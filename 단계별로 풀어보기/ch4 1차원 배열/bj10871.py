#10871, X보다 작은 수
#배열을 입력받고 X보다 작은 수를 찾는 문제

N, X = map(int, input().split())
A = list(map(int, input().split()))

for i in range(len(A)):
    if A[i] < X : print(f"{A[i]}", end = " ")