N = int(input())
scorelist = list(map(int, input().split()))

newscore = []
for score in scorelist :
    newscore.append(score / max(scorelist) * 100)
avg = sum(newscore) / N
print(avg)