#2562, 최댓값
#최댓값이 어디에 있는지 찾는 문제

nlist = []
for i in range(9) :
    num = int(input())
    nlist.append(num)

print(max(nlist))
print(nlist.index(max(nlist))+1)