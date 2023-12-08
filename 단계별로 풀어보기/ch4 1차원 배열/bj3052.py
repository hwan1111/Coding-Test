#3052, 나머지
#배열을 활용하여 서로 다른 값의 개수를 찾는 문제

B = []
for i in range(10):
    A = int(input())
    B.append(A%42)
    setB = set(B)
    listB = list(setB)

print(len(listB))