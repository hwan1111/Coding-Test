#2501, 약수 구하기
#주어진 수의 약수를 구하는 문제

mod = []
n, k = map(int, input().split())

for i in range(1, n+1):
    if n%i == 0:
        mod.append(i)

if k > len(mod):
    print(0)
else:
    print(mod[k-1])