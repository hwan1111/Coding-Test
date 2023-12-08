while True:
    a, b = map(int, input().split())
    if a >= 10000 and b >= 10000:
        break
    elif a == 0 and b == 0:
        break
    else:
        if a < b:
            if b%a == 0:
                print("factor")
            else:
                print("neither")
        elif a > b:
            if a%b == 0:
                print("multiple")
            else:
                print("neither")
        elif a == b:
            break