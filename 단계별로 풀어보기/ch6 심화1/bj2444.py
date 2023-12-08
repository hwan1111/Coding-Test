#2444, 별 찍기 -7
#🌟

n = int(input())

for i in range(1, 2*n, 2) :
    s = "*"*i
    print(s.center(2*n-1))
for i in range(2*n-3, 0, -2):
    s = "*"*i
    print(s.center(2*n-1))