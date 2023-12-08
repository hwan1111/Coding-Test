def shoms_movie(N):
    num = 666
    cnt = 0

    while True:
        if '666' in str(num):
            cnt += 1
        if cnt == N:
            return num
            break
        num += 1

N = int(input())
print(shoms_movie(N))