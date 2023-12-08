#11022, A+B -8
#A+B를 바로 위 문제보다 아름답게 출력하는 문제

T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    print(f"Case #{i+1}: {A} + {B} = {A+B}")