#9506, 약수들의 합
#약수를 구하면서 주어진 수가 완전수인지 판별하는 문제
#완전수: 어떤 숫자 n이 자신을 제외한 모든 약수들의 합과 같으면, 그 수를 완전수라고 한다 ex) 6 = 1 + 2 + 3

while True:
    mod = []
    n = int(input())
    if 2 < n < 100000:
        for i in range(1, n):
            if n%i == 0:
                mod.append(i)

        if sum(mod) == n:
            print(f"{n} = ", end = "")
            for j in range(len(mod)-1):
                print(f"{mod[j]}", end = " + ")
            print(f"{mod[-1]}")
        else:
            print(f"{n} is NOT perfect.")
    elif n == -1:
        break
    else:
        break