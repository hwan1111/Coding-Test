#1546, 평균
#평균을 조작하는 문제

n = int(input())
score = list(map(int, input().split()))

for i in range(len(score)):
    score[i] = score[i]/max(score)*100

print(sum(score)/len(score))