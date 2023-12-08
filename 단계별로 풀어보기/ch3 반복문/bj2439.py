#2439, 별 찍기 -2
#별을 찍는 문제 2

N = int(input())

for i in range(1, N+1):
    print((N-i)*" "+"*"*i)