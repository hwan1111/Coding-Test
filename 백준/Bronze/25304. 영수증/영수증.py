price = int(input())
N = int(input())
sum = 0
for i in range(N) :
    a, b = map(int,input().split())
    s = a * b
    sum += s

if sum == price :
    print("Yes")
else : print("No")