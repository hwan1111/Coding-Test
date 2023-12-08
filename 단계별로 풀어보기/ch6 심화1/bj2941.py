#2941, 크로아티아 알파벳
#두세 문자가 한 글자로 묶일 수 있을 때 글자의 수를 세는 문제

Croatia = ["c=", "dz=", "lj", "s=", "c-", "d-", "nj", "z="]
word = input()

for i in Croatia:
    word = word.replace(i, 'a')

print(len(word))