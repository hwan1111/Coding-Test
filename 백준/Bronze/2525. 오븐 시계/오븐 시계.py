h, m = map(int, input().split(" "))
m2 = int(input())

hm = h*60 + m;
hm += m2;
print((hm // 60)%24, hm % 60 )