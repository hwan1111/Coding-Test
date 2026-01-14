import sys

input = sys.stdin.readline

def fast_print(N):
    sys.stdout.write(str( N ) + '\n')

N = int(input())
for i in range(1, N + 1):
    fast_print(i)