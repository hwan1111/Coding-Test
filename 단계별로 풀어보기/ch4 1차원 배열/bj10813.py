#10813, 공 바꾸기
#배열의 값을 교환하는 문제

n, m = map(int, input().split())
basket = [x for x in range(1, n+1)]
for _ in range(m):
    i, j = map(int, input().split())
    basket[i-1], basket[j-1] = basket[j-1], basket[i-1]     #스왑

for s in range(len(basket)):
    print(basket[s], end = " ")