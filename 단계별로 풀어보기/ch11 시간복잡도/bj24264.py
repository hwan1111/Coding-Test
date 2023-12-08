#24264, 알고리즘 수업 - 알고리즘의 수행 시간 3
#...실행 횟수가 "대략적으로" 얼마나 빨리 커지는지는 비교적 간단하게 알 수 있습니다. 이 문제들에서 출력의 두 번째 줄이 바로 그것입니다

"""
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n
        for j <- 1 to n
            sum <- sum + A[i] × A[j]; # 코드1
    return sum;
}
"""

n = int(input())

print(n**2)
print(2)