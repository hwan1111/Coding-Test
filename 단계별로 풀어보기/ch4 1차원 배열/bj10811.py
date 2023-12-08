#10811, 바구니 뒤집기
#배열을 뒤집는 문제

N, M = map(int, input().split())
arr = [x for x in range(1, N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    s = (j-i+1)//2

    for k in range(s):
        arr[i+k-1], arr[j-k-1] = arr[j-k-1], arr[i+k-1]

for i in range(len(arr)):
    print(arr[i], end = " ")