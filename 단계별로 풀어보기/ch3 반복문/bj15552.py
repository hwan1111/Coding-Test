import sys
import time
T = int(sys.stdin.readline())

for i in range(T) :
    start = time.time()
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)
    end = time.time()

print(end - start)
