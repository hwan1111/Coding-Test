#2292, 벌집
#벌집이 형성되는 규칙에 따라 벌집의 위치를 구하는 문제

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