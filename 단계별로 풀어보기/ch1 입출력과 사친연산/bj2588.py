#2588, 곱셈
#빈 칸에 들어갈 수는?

A = int(input())
B = int(input())

C = ((B//10**0)%10)*A
D = ((B//10**1)%10)*A
E = ((B//10**2)%10)*A

print(C)
print(D)
print(E)
print(E*100+D*10+C)