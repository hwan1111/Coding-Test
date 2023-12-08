#1330, 두 수 비교하기
#두 수를 비교한 결과를 출력하는 문제

A, B = map(int, input().split())

if A > B : print(">")
elif A < B : print("<")
else : print("=")