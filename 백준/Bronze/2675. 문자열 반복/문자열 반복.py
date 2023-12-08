T = int(input())
for _ in range(T) :
    R, S = map(str, input().split())
    cycle = int(R)
    for i in range(len(S)) :
        print(cycle*S[i], end = "")
    print()