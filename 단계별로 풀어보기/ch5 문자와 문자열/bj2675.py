#2675, 문자열 반복
#각 문자를 반복하여 출력하는 문제

T = int(input())
for _ in range(T):
    s, r = map(str, input().split())
    for j in range(len(r)):
        print(r[j]*int(s), end = "")
    print()