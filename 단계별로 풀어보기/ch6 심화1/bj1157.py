#1157, 단어 공부
#주어진 단어에서 가장 많이 사용된 알파벳을 출력하는 문제

word = input().lower()
word_list = list(set(word))
cnt = []

for i in word_list:
    count = word.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(word_list[(cnt.index(max(cnt)))].upper())