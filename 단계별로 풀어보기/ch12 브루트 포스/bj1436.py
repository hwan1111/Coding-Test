#1436, 영화감독 숌
#N번째 종말의 수가 나올 때까지 차례대로 시도하는 문제

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