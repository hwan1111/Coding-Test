def solution(price, money, cnt):
    charge = 0
    for i in range(1, cnt + 1):
        charge += price * i
        
    if money - charge < 0:
        return abs(money - charge)
    else:
        return 0