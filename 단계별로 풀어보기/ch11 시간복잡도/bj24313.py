#24313, 알고리즘 수업 - 점근적 표기 1
#시간 복잡도는 빅-O표기법으로 표현할 수 있습니다. 정확한 정의보다는 "이 함수에 비례한다" 정도만 기억해도 무방합니다.

a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

if ((a1*n0 + a0 <= c*n0) and (a1 <= c)):
    print(1)
else:
    print(0)