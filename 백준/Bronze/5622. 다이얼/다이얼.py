dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WYXZ"]
S = input()
Set = 0
for j in range(len(S)) :
    for i in dial :
        if S[j] in i :
            Set += dial.index(i) + 3
print(Set)