#1316, 그룹 단어 체커
#조건에 맞는 문자열을 찾는 문제

N = int(input())
count = N
for i in range(N):
    word = list(input())
    for j in range(len(word)-1):
        if word[j] == word[j+1]: pass
        elif word[j] in word[j+1:]:
            count -= 1
            break

print(count)