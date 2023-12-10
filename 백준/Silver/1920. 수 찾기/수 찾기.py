import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().rstrip().split()))
A.sort()

M = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

for num in arr:
    left = 0
    right = N-1
    isExist = False
    while left <= right:
        mid = (left + right) // 2

        if num == A[mid]:
            isExist = True
            print(1)
            break
        elif num > A[mid]:
            left = mid + 1
        elif num < A[mid]:
            right = mid - 1
    
    if not isExist:
        print(0)