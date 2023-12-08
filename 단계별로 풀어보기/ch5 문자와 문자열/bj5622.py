#5622, 다이얼
#규칙에 따라 문자에 대응하는 수를 출력하는 문제

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
s = input()
Set = 0
for i in range(len(s)):
    for j in dial:
        if s[i] in j:
            Set += dial.index(j) + 3

print(Set)