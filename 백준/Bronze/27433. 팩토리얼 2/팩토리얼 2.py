def Fact(num) :
    if num == 1 or num == 0 :
        return 1
    else :
        return num * Fact(num - 1)
        num -= 1

num = int(input())

print(Fact(num))