#1152, 단어의 개수
#단어의 개수를 구하는 문제

S = input()
count = 0
for i in range(len(S)) :
    if S[i] == " ":
        count += 1

if S[0] == " " or S[-1] == " " :
        count -= 1

print(count+1)