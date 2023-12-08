#24265, 알고리즘 수업 - 알고리즘의 수행 시간 4
#n이 커질수록 n과 n²의 차이는 어마어마하게 벌어지기 때문에,

"""
MenOfPassion(A[], n) {
    sum <- 0;
    for i <- 1 to n - 1
        for j <- i + 1 to n
            sum <- sum + A[i] × A[j]; # 코드1
    return sum;
}
"""

n = int(input())
print((n**2-n)//2)
print(2)