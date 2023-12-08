#2798, 블랙잭
#세 장의 카드를 고르는 모든 경우를 고려하는 문제

N, M = map(int, input().split())
cards = list(map(int, input().split()))
result = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            total = cards[i] + cards[j] + cards[k]

            if result < total <= M:
                result = total

print(result)