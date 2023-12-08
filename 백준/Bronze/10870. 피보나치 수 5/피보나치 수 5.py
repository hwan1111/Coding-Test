def Fibo(num) :
    f, s = 0, 1
    for i in range(num) :
        f, s = s, f + s
    return f

num = int(input())

print(Fibo(num))