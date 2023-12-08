#10810, 공넣기
#배열에 값을 쓰는 문제

n, m = map(int, input().split())    #n과 m을 입력 받음
basket = [0]*n      #모든 원소가 0이고 길이가 n인 리스트 생성
for _ in range(m):  #m번 반복
    i, j, k = map(int, input().split())
    while i <= j:   #i번째부터 j번째 까지
        basket[i-1] = k     #바스켓은 1번부터 있으니 조정
        i += 1

for s in range(n):
    print(basket[s], end = " ")