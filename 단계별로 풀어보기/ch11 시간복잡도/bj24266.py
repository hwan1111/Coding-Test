#24266, 알고리즘 수업 - 알고리즘의 수행 시간 5
#"대략적으로"만 파악해도 자신의 코드가 시간 초과가 날 지 아닐지를 어느 정도 예측할 수 있습니다.

"""
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n
        for j <- 1 to n
            for k <- 1 to n
                sum <- sum + A[i] × A[j] × A[k]; # 코드1
    return sum;
}
"""

n = int(input())
print(n**3)
print(3)