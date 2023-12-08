T = int(input())

for i in range(T):
    n = int(input())
    print("++++ "*int(n//5) + "|"*int(n%5))