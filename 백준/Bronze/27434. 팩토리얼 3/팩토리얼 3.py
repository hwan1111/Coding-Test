def Fac(num) :
    res = 1
    for i in range(1, num + 1) :
        res = res * i
    return res

num = int(input())
print(Fac(num))