#10818, 최소, 최대
#최솟값과 최댓값을 찾는 문제

N = int(input())
num = list(map(int, input().split()))

print(f"{min(num)} {max(num)}")