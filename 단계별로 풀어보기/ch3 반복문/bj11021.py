#11021, A+B -7
#A+B를 조금 더 아름답게 출력하는 문제

T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    print(f"Case #{i+1}: {A+B}")