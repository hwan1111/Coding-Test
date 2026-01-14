T = int(input())

for _ in range(T):
    x = input()
    list_x = x.split('X')

    result = 0

    for i in list_x:
        result += (len(i) * (len(i) + 1)) // 2

    print(result)