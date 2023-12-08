#2720, 세탁소 사장 동혁
#💰

T = int(input())
for _ in range(T):
    C = int(input())
    Quarter = C//25
    Dime = (C-25*Quarter)//10
    Nickel = (C-25*Quarter-10*Dime)//5
    Penny = (C-25*Quarter-10*Dime-5*Nickel)
    print(Quarter, Dime, Nickel, Penny)