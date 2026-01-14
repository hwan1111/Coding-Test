from collections import Counter

A = int(input())
B = int(input())
C = int(input())

result = str(A * B * C)
counter = Counter(result)
for i in range(10):
    print(counter.get(str(i), 0))