#8393, 합
#1부터 N까지의 합을 구하는 문제. 물론 반복문 없이 풀 수도 있습니다.

n = int(input())
sum = 0
for i in range(n+1) :
    sum += i

print(sum)