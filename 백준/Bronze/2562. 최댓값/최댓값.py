alist = []
for i in range(9) :
    a = int(input())
    alist.append(a)
b = max(alist)
c = alist.index(b)

print(f"{b} {c + 1}")