#5073, 삼각형과 세 변
#변의 길이를 보고 삼각형을 판별하고 분류하는 문제

while True:
    a, b, c = list(map(int, input().split()))
    if a == 0 and b == 0 and c == 0:
        break
    elif max(a, b, c) < (a+b+c) - max(a, b, c):
        if a == b == c:
            print("Equilateral")
        elif (a == b and a != c) or (b == c and b != a) or (c == a and c != b):
            print("Isosceles")
        elif a != b and b != c and c != a:
            print("Scalene")
    else:
        print("Invalid")