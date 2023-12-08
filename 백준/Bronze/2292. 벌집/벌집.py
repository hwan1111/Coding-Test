count = 0
i = 0
N = int(input())
if N == 1:
    print(1)
else: 
    while N >=2:
        count +=1
        N -= 6*i
        i += 1
    print(count)