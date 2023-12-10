import sys

N = int(sys.stdin.readline())
A = set(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().rstrip().split()))

for num in arr:
    print(1) if num in A else print(0)